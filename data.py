"""
Data content for Pot Odds Learning Application based on the prototype
"""

# Content organized by topics
learn_data = {
    "WhatArePotOdds": [
        {
            "type": "text_content",
            "title": "What are pot odds?",
            "content": "Pot odds are the ratio between the current size of the pot and the cost of a contemplated call.",
            "image": "/static/images/image1.png",
        }
    ],
    "WhenDoPotOddsMatter": [
        {
            "type": "text_content",
            "title": "When do pot odds matter?",
            "content": "Pot odds matter in every poker game situation where you're deciding whether to call a bet, especially when considering drawing hands or bluffing.",
            "image": "/static/images/image3.png",
        }
    ],
    "EstimatingEquity": [
        {
            "type": "text_content",
            "title": "Estimating Equity",
            "content": 'To estimate your equity in poker, understand that equity represents the portion of the pot you expect to win based on your chances of winning. You can roughly calculate this by considering your "outs" (cards that improve your hand) and applying the "Rule of 4 and 2"',
            "image": "/static/images/image4.png",
        },
        {
            "type": "text_content",
            "title": "Rule of 4 and 2 - Poker Outs Chart",
            "content": "The Rule of 4 and 2 is a quick way to estimate your equity from the number of outs you have. RULE OF 4: X4 (FLOP TO TURN AND RIVER), RULE OF 2: X2 (TURN TO RIVER)",
            "image": "/static/images/image5.png",
        },
    ],
    "HowToUsePotOdds": [
        {
            "type": "text_content",
            "title": "How to use pot odds - Step 1",
            "content": "Calculate the Pot Odds: Determine the current pot size. Determine the size of the bet you're facing. Calculate the new pot size after you call (current pot + your call).",
            "image": "/static/images/image2.png",
        },
        {
            "type": "text_content",
            "title": "How to use pot odds - Step 2 & 3",
            "content": "Compare Pot Odds to Required Equity: If the pot odds are better than the equity you need to win, it's generally a good call. If the pot odds are worse than the equity you need to win, it's generally a good fold.",
            "image": "/static/images/image4.png",
        },
        {
            "type": "text_content",
            "title": "Video: Pot Odds in Action",
            "content": """
                Watch this quick video for a real-game example of how pot odds work:
                <br><br>
            <iframe width="560" height="315"
                src="https://www.youtube.com/embed/_OFM3AAcBD8?si=NSOWSlrd-5uwTjmr"
                title="YouTube video player"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                referrerpolicy="strict-origin-when-cross-origin"
                allowfullscreen>
                </iframe>
                 """,
        }

    ],
}

# Quiz questions and answers
quiz_data = {
    "question_1": [
        {
            "question": "Flush Draw: Pot: $80, Bet: $20, Hand: 2 hearts in hand + 2 on board (9 outs)",
            "options": ["Yes", "No"],
            "correct_answer": 0,
            "explanation": "Yes! Pot odds 20/100 = 20%, equity ≈ 36%",
            "image": "/static/images/image2.png",
        }
    ],
    "question_2": [
        {
            "question": "Gutshot Straight Draw: Pot: $90, Bet: $30, 4 outs (inside straight)",
            "options": ["Yes", "No"],
            "correct_answer": 1,
            "explanation": "No! Your equity (16%) is less than the pot odds (25%). This call would lose money in the long run.",
            "image": "/static/images/image3.png",
        }
    ],
    "question_3": [
        {
            "question": "Overcards: Pot: $120, Bet: $40, You hold AK, board is 9-7-2 rainbow → no real outs",
            "options": ["Yes", "No"],
            "correct_answer": 1,
            "explanation": "No! Your equity is weak with only 6 outs max",
            "image": "/static/images/image4.png",
        }
    ],
    "question_4": [
        {
            "question": "Paired Board: Pot: $100, Bet: $50, You have 10♣ 10♦, board: Q♣ Q♦ 2♠",
            "options": ["Yes", "No"],
            "correct_answer": 1,
            "explanation": "No! Your equity is extremely low. Calling 33% pot odds with 8% equity is a mistake.",
            "image": "/static/images/image1.png",
        }
    ],
    "question_5": [
        {
            "question": "Combo Draw: Pot: $150, Bet: $50, You hold 5♠ 6♠, board: 7♠ 8♠ Q♥, 15 outs (combo draw) → Equity ≈ 60%",
            "options": ["Yes", "No"],
            "correct_answer": 0,
            "explanation": "Yes! Massive equity (60%) vs 25% pot odds makes this a slam-dunk call (and sometimes a raise!)",
            "image": "/static/images/image5.png",
        }
    ],
}

# Order of topics for navigation
topic_order = [
    "WhatArePotOdds",
    "WhenDoPotOddsMatter",
    "EstimatingEquity",
    "HowToUsePotOdds",
]

# Practice Quiz questions and answers
practice_quiz_data = {
    "question_1": [
        {
            "question": "Basic Pot Odds: Pot: $50, Bet: $25, What are your pot odds?",
            "options": ["3:1", "2:1", "1:2", "1:3"],
            "correct_answer": 0,
            "explanation": "Pot odds are calculated as (pot + bet) : bet = $75 : $25 = 3:1",
            "image": "/static/images/image2.png",
        }
    ],
    "question_2": [
        {
            "question": "Required Equity: Pot odds are 4:1. What equity do you need to break even?",
            "options": ["40%", "25%", "20%", "10%"],
            "correct_answer": 2,
            "explanation": "With 4:1 pot odds, you need 1/(4+1) = 1/5 = 20% equity to break even",
            "image": "/static/images/image3.png",
        }
    ],
    "question_3": [
        {
            "question": "Outs to Equity: You have 8 outs on the flop. What's your approximate equity?",
            "options": ["16%", "24%", "32%", "40%"],
            "correct_answer": 2,
            "explanation": "Using the Rule of 4, with 8 outs, your equity is approximately 8 × 4 = 32%",
            "image": "/static/images/image5.png",
        }
    ],
}
