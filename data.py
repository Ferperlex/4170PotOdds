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

# Quiz questions and answers - IMPROVED VERSION
quiz_data = {
    "question_1": [
        {
            "question": "Flush Draw: Pot: $80, Bet: $20, Hand: 2 hearts in hand + 2 on board (9 outs = 36% equity)",
            "options": ["Call (Yes)", "Fold (No)"],
            "correct_answer": 0,
            "explanation": "Yes, call! The pot odds are 20/100 = 20%, and your equity with a flush draw is about 36%. Since your equity (36%) exceeds the pot odds (20%), this is a profitable call.",
            "image": "/static/images/image2.png",
        }
    ],
    "question_2": [
        {
            "question": "Gutshot Straight Draw: Pot: $90, Bet: $30, Hand: Inside straight draw (4 outs = 16% equity)",
            "options": ["Call (Yes)", "Fold (No)"],
            "correct_answer": 1,
            "explanation": "No, fold! Your equity (16%) is less than the pot odds (25%). This call would lose money in the long run because you aren't getting the right price to chase your draw.",
            "image": "/static/images/image3.png",
        }
    ],
    "question_3": [
        {
            "question": "Overcards: Pot: $120, Bet: $40, Hand: AK, Board: 9-7-2 rainbow (6 outs = 24% equity)",
            "options": ["Call (Yes)", "Fold (No)"],
            "correct_answer": 1,
            "explanation": "No, fold! Your pot odds are 40/160 = 25%. With just overcards (6 outs), your equity is about 24%, which is slightly less than the pot odds required to call profitably.",
            "image": "/static/images/image4.png",
        }
    ],
    "question_4": [
        {
            "question": "Paired Board: Pot: $100, Bet: $50, Hand: 10♣ 10♦, Board: Q♣ Q♦ 2♠ (2 outs = 8% equity)",
            "options": ["Call (Yes)", "Fold (No)"],
            "correct_answer": 1,
            "explanation": "No, fold! Your pot odds are 50/150 = 33%, but your equity with a small pocket pair against a paired board is only about 8%. This is a clear fold.",
            "image": "/static/images/image1.png",
        }
    ],
    "question_5": [
        {
            "question": "Combo Draw: Pot: $150, Bet: $50, Hand: 5♠ 6♠, Board: 7♠ 8♠ Q♥ (15 outs = 60% equity)",
            "options": ["Call (Yes)", "Fold (No)"],
            "correct_answer": 0,
            "explanation": "Yes, call! Your pot odds are 50/200 = 25%, but with a flush draw + straight draw combo (15 outs), your equity is around 60%. This is a slam-dunk call and possibly even a raise opportunity!",
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

# Practice Quiz questions and answers - IMPROVED VERSION
practice_quiz_data = {
    "question_1": [
        {
            "question": "If the pot is $50 and your opponent bets $25, what are your pot odds?",
            "options": ["3:1", "2:1", "1:2", "1:3"],
            "correct_answer": 0,
            "explanation": "Pot odds are calculated as (current pot + opponent's bet) : cost to call = $75 : $25 = 3:1",
            "image": "/static/images/image2.png",
        }
    ],
    "question_2": [
        {
            "question": "If your pot odds are 4:1, what minimum equity percentage do you need to break even?",
            "options": ["40%", "25%", "20%", "10%"],
            "correct_answer": 2,
            "explanation": "With 4:1 pot odds, you need 1/(4+1) = 1/5 = 20% equity to break even. If your equity is higher than 20%, the call is profitable.",
            "image": "/static/images/image3.png",
        }
    ],
    "question_3": [
        {
            "question": "You have 8 outs on the flop. Using the Rule of 4, what's your approximate equity percentage?",
            "options": ["16%", "24%", "32%", "40%"],
            "correct_answer": 2,
            "explanation": "Using the Rule of 4, with 8 outs, your equity is approximately 8 × 4 = 32%. This is your approximate chance of hitting your outs by the river.",
            "image": "/static/images/image5.png",
        }
    ],
}
