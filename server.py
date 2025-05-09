from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from data import learn_data, quiz_data, practice_quiz_data, topic_order
import logging
import json
import os
from datetime import datetime

# Configuration
DEBUG_MODE = True
SECRET_KEY = "pot_odds_secret_key"  # In production, use environment variables
SESSION_LIFETIME = 30  # minutes

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="app.log",
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = SECRET_KEY


def initialize_session():
    """Initialize or get the user session data."""
    if "user_progress" not in session:
        session["user_progress"] = {
            "current_topic": 0,
            "current_slide": 0,
            "quiz_answers": [],
            "timestamps": [],
            "time_analytics": [],
        }
    return session["user_progress"]


def save_progress(progress_data):
    """
    Save user progress to a file for persistence.

    In a real application, this would save to a database.
    """
    try:
        if not os.path.exists("user_data"):
            os.makedirs("user_data")

        # Use a timestamp as a simple identifier
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        with open(f"user_data/progress_{timestamp}.json", "w") as f:
            json.dump(progress_data, f)

        logger.info(f"Saved progress data: progress_{timestamp}.json")
    except Exception as e:
        logger.error(f"Error saving progress: {e}")


def track_time_spent():
    """Track time spent on the current page."""
    user_progress = initialize_session()

    if "page_start_time" in session:
        start_time = datetime.fromisoformat(session["page_start_time"])
        time_spent = (datetime.now() - start_time).total_seconds()

        user_progress["time_analytics"].append(
            {
                "page": request.path,
                "time_spent": time_spent,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )

        session["user_progress"] = user_progress

    session["page_start_time"] = datetime.now().isoformat()
    return user_progress


@app.route("/")
def index():
    """Render the homepage and initialize user session."""
    try:
        logger.info("User accessed homepage")
        session["user_progress"] = {
            "current_topic": 0,
            "current_slide": 0,
            "quiz_answers": [],
            "timestamps": [],
            "time_analytics": [],
        }
        session["page_start_time"] = datetime.now().isoformat()
        return render_template("index.html")
    except Exception as e:
        logger.error(f"Error on homepage: {e}")
        return "An error occurred. Please try again.", 500


@app.route("/learn/<string:topic>/<int:slide_number>")
def learn(topic, slide_number):
    """
    Handle learning content pages.

    Parameters:
        topic (str): The topic identifier
        slide_number (int): The slide number (1-indexed)
    """
    try:
        user_progress = track_time_spent()

        # Update current position
        user_progress["current_topic"] = (
            topic_order.index(topic) if topic in topic_order else 0
        )
        user_progress["current_slide"] = slide_number - 1  # Adjust to 0-based index

        # Record access timestamp
        user_progress["timestamps"].append(
            {
                "topic": topic,
                "slide": slide_number,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
        session["user_progress"] = user_progress

        # Get topic data
        slide_number -= 1
        topic_data = learn_data.get(topic, [])

        # Handle navigation to next topic if current slide doesn't exist
        if slide_number < 0 or slide_number >= len(topic_data):
            next_topic_index = (
                topic_order.index(topic) + 1 if topic in topic_order else 0
            )
            if next_topic_index >= len(topic_order):
                logger.info(
                    f"User completed all learning content, redirecting to transition"
                )
                return redirect(url_for("transition"))
            else:
                next_topic = topic_order[next_topic_index]
                logger.info(f"Moving to next topic: {next_topic}")
                return redirect(url_for("learn", topic=next_topic, slide_number=1))

        # Get slide data
        slide_data = topic_data[slide_number]
        content_type = slide_data.get("type", "text_content")
        template_name = f"{content_type}.html"

        # Calculate next slide URL
        next_slide_number = slide_number + 2
        next_topic_index = topic_order.index(topic) if topic in topic_order else 0

        if slide_number >= len(topic_data) - 1:
            next_topic_index += 1
            if next_topic_index >= len(topic_order):
                next_slide_url = url_for("transition")
            else:
                next_topic = topic_order[next_topic_index]
                next_slide_url = url_for("learn", topic=next_topic, slide_number=1)
        else:
            next_slide_url = url_for(
                "learn", topic=topic, slide_number=next_slide_number
            )

        # Calculate previous slide URL
        prev_slide_number = slide_number
        prev_topic_index = topic_order.index(topic) if topic in topic_order else 0

        if slide_number <= 0:
            prev_topic_index -= 1
            if prev_topic_index < 0:
                prev_slide_url = url_for("index")
            else:
                prev_topic = topic_order[prev_topic_index]
                prev_topic_data = learn_data.get(prev_topic, [])
                prev_slide_url = url_for(
                    "learn", topic=prev_topic, slide_number=len(prev_topic_data)
                )
        else:
            prev_slide_url = url_for(
                "learn", topic=topic, slide_number=prev_slide_number
            )

        logger.info(f"Displaying learning content: {topic}, slide {slide_number + 1}")

        return render_template(
            template_name,
            title=slide_data.get("title", ""),
            content=slide_data.get("content", ""),
            image=slide_data.get("image", ""),
            next_url=next_slide_url,
            prev_url=prev_slide_url,
            topic=topic,
            current_topic_index=next_topic_index,
            total_topics=len(topic_order),
            topic_order=topic_order,
        )
    except Exception as e:
        logger.error(f"Error in learn route: {e}")
        return (
            "An error occurred while displaying learning content. Please try again.",
            500,
        )


@app.route("/transition")
def transition():
    """Show transition page between learning and quiz."""
    track_time_spent()
    logger.info("User accessing transition page")
    return render_template("transition.html", next_url=url_for("quiz", q_number=1))


@app.route("/practice_quiz/<int:q_number>", methods=["GET", "POST"])
def practice_quiz(q_number):
    """
    Handle practice quiz questions and answers.

    GET: Display the practice quiz question
    POST: Process the user's answer and redirect to the next question

    Parameters:
        q_number (int): The question number (1-indexed)
    """
    try:
        user_progress = track_time_spent()

        if request.method == "GET":
            question_key = f"question_{q_number}"
            question_data = practice_quiz_data.get(question_key, [])

            if not question_data:
                logger.warning(f"Invalid practice quiz question number: {q_number}")
                return redirect(url_for("index"))

            question = question_data[0]["question"]
            options = question_data[0]["options"]
            image = question_data[0].get("image", None)

            # Record access timestamp
            user_progress["timestamps"].append(
                {
                    "practice_quiz_question": q_number,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            )
            session["user_progress"] = user_progress

            logger.info(f"Displaying practice quiz question {q_number}")

            return render_template(
                "practice_quiz.html",
                question=question,
                options=options,
                q_number=q_number,
                next_url=url_for("practice_quiz", q_number=q_number),
                total_questions=len(practice_quiz_data),
                image=image,
            )

        elif request.method == "POST":
            try:
                user_answer = request.form.get("answer")

                if user_answer is None:
                    logger.warning("No answer provided in form submission")
                    return redirect(url_for("practice_quiz", q_number=q_number))

                # Store the answer
                if "practice_quiz_answers" not in user_progress:
                    user_progress["practice_quiz_answers"] = []

                if len(user_progress["practice_quiz_answers"]) < q_number:
                    user_progress["practice_quiz_answers"].append(user_answer)
                else:
                    user_progress["practice_quiz_answers"][q_number - 1] = user_answer

                session["user_progress"] = user_progress

                logger.info(
                    f"Received answer for practice quiz question {q_number}: {user_answer}"
                )

                # Navigate to next question or results
                next_q_number = q_number + 1
                if f"question_{next_q_number}" in practice_quiz_data:
                    next_url = url_for("practice_quiz", q_number=next_q_number)
                else:
                    next_url = url_for("practice_quiz_results")

                return redirect(next_url)
            except Exception as e:
                logger.error(f"Error processing practice quiz answer: {e}")
                return (
                    "An error occurred while processing your answer. Please try again.",
                    500,
                )
    except Exception as e:
        logger.error(f"Error in practice quiz route: {e}")
        return (
            "An error occurred while displaying the practice quiz. Please try again.",
            500,
        )


@app.route("/practice_quiz_results")
def practice_quiz_results():
    """Calculate and display practice quiz results."""
    try:
        user_progress = track_time_spent()

        # Initialize practice quiz answers if not present
        if "practice_quiz_answers" not in user_progress:
            user_progress["practice_quiz_answers"] = []
            session["user_progress"] = user_progress

        user_answers = user_progress["practice_quiz_answers"]

        score = 0
        results = []

        for q_number, user_answer in enumerate(user_answers, start=1):
            question_key = f"question_{q_number}"
            question_data = practice_quiz_data.get(question_key, [])

            if question_data:
                correct_answer_index = question_data[0]["correct_answer"]
                is_correct = int(user_answer) == correct_answer_index

                if is_correct:
                    score += 1

                results.append(
                    {
                        "question": question_data[0]["question"],
                        "user_answer": question_data[0]["options"][int(user_answer)],
                        "correct_answer": question_data[0]["options"][
                            correct_answer_index
                        ],
                        "is_correct": is_correct,
                        "explanation": question_data[0].get("explanation", ""),
                        "image": question_data[0].get("image", ""),
                    }
                )

        total_questions = len(practice_quiz_data)
        percentage_score = (score / total_questions) * 100 if total_questions > 0 else 0

        # Record completion
        user_progress["timestamps"].append(
            {
                "practice_quiz_completed": True,
                "score": score,
                "percentage": percentage_score,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
        session["user_progress"] = user_progress

        # Save the progress for analytics
        save_progress(user_progress)

        logger.info(
            f"Practice quiz completed. Score: {score}/{total_questions} ({percentage_score:.2f}%)"
        )

        return render_template(
            "practice_quiz_results.html",
            score=score,
            percentage=percentage_score,
            total_questions=total_questions,
            results=results,
        )
    except Exception as e:
        logger.error(f"Error in practice quiz results route: {e}")
        return (
            "An error occurred while calculating your practice quiz results. Please try again.",
            500,
        )


@app.route("/quiz/<int:q_number>", methods=["GET", "POST"])
def quiz(q_number):
    """
    Handle quiz questions and answers.

    GET: Display the quiz question
    POST: Process the user's answer and redirect to the next question

    Parameters:
        q_number (int): The question number (1-indexed)
    """
    try:
        user_progress = track_time_spent()

        if request.method == "GET":
            question_key = f"question_{q_number}"
            question_data = quiz_data.get(question_key, [])

            if not question_data:
                logger.warning(f"Invalid question number: {q_number}")
                return redirect(url_for("index"))

            question = question_data[0]["question"]
            options = question_data[0]["options"]
            image = question_data[0].get("image", None)

            # Record access timestamp
            user_progress["timestamps"].append(
                {
                    "quiz_question": q_number,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            )
            session["user_progress"] = user_progress

            logger.info(f"Displaying quiz question {q_number}")

            return render_template(
                "quiz.html",
                question=question,
                options=options,
                q_number=q_number,
                next_url=url_for("quiz", q_number=q_number),
                total_questions=len(quiz_data),
                image=image,
            )

        elif request.method == "POST":
            try:
                user_answer = request.form.get("answer")

                if user_answer is None:
                    logger.warning("No answer provided in form submission")
                    return redirect(url_for("quiz", q_number=q_number))

                # Store the answer
                if len(user_progress["quiz_answers"]) < q_number:
                    user_progress["quiz_answers"].append(user_answer)
                else:
                    user_progress["quiz_answers"][q_number - 1] = user_answer

                session["user_progress"] = user_progress

                logger.info(f"Received answer for question {q_number}: {user_answer}")

                # Navigate to next question or results
                next_q_number = q_number + 1
                if f"question_{next_q_number}" in quiz_data:
                    next_url = url_for("quiz", q_number=next_q_number)
                else:
                    next_url = url_for("quiz_results")

                return redirect(next_url)
            except Exception as e:
                logger.error(f"Error processing quiz answer: {e}")
                return (
                    "An error occurred while processing your answer. Please try again.",
                    500,
                )
    except Exception as e:
        logger.error(f"Error in quiz route: {e}")
        return "An error occurred while displaying the quiz. Please try again.", 500


@app.route("/quiz_results")
def quiz_results():
    """Calculate and display quiz results."""
    try:
        user_progress = track_time_spent()
        user_answers = user_progress["quiz_answers"]

        score = 0
        results = []

        for q_number, user_answer in enumerate(user_answers, start=1):
            question_key = f"question_{q_number}"
            question_data = quiz_data.get(question_key, [])

            if question_data:
                correct_answer_index = question_data[0]["correct_answer"]
                is_correct = int(user_answer) == correct_answer_index

                if is_correct:
                    score += 1

                results.append(
                    {
                        "question": question_data[0]["question"],
                        "user_answer": question_data[0]["options"][int(user_answer)],
                        "correct_answer": question_data[0]["options"][
                            correct_answer_index
                        ],
                        "is_correct": is_correct,
                        "explanation": question_data[0].get("explanation", ""),
                        "image": question_data[0].get("image", ""),
                    }
                )

        total_questions = len(quiz_data)
        percentage_score = (score / total_questions) * 100 if total_questions > 0 else 0

        # Record completion
        user_progress["timestamps"].append(
            {
                "quiz_completed": True,
                "score": score,
                "percentage": percentage_score,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
        session["user_progress"] = user_progress

        # Save the progress for analytics
        save_progress(user_progress)

        logger.info(
            f"Quiz completed. Score: {score}/{total_questions} ({percentage_score:.2f}%)"
        )

        return render_template(
            "quiz_results.html",
            score=score,
            percentage=percentage_score,
            total_questions=total_questions,
            results=results,
        )
    except Exception as e:
        logger.error(f"Error in quiz_results route: {e}")
        return (
            "An error occurred while calculating your quiz results. Please try again.",
            500,
        )


@app.route("/main-menu")
def main_menu():
    """Display the main menu page."""
    track_time_spent()
    logger.info("User accessing main menu")
    return render_template("main_menu.html")


@app.route("/feedback", methods=["POST"])
def submit_feedback():
    """Handle user feedback submission."""
    try:
        feedback = request.form.get("feedback_text")
        rating = request.form.get("rating")

        if not feedback:
            logger.warning("Empty feedback submitted")
            return redirect(url_for("index"))

        # Store feedback in a file
        if not os.path.exists("user_data"):
            os.makedirs("user_data")

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        with open(f"user_data/feedback_{timestamp}.txt", "w") as f:
            f.write(f"Rating: {rating}\n")
            f.write(f"Feedback: {feedback}\n")
            f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        logger.info(f"Feedback submitted: rating={rating}")
        return redirect(url_for("thank_you"))
    except Exception as e:
        logger.error(f"Error submitting feedback: {e}")
        return (
            "An error occurred while submitting your feedback. Please try again.",
            500,
        )


@app.route("/thank-you")
def thank_you():
    """Display thank you page after feedback submission."""
    return render_template("thank_you.html")


@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    logger.warning(f"404 error: {request.path}")
    return render_template("error.html", error_code=404, message="Page not found"), 404


@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors."""
    logger.error(f"500 error: {str(e)}")
    return (
        render_template("error.html", error_code=500, message="Internal server error"),
        500,
    )


if __name__ == "__main__":
    app.run(debug=DEBUG_MODE)
