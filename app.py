import streamlit as st

scenario = {
    "title": "Global Expansion Dilemma",
    "description": "Your company is considering expanding into a new international market. Recent reports suggest potential ethical concerns in the target country's business practices.",
    "questions": [
        {
            "question": "How do you approach the decision to expand?",
            "choices": [
                "Proceed with expansion, prioritizing business growth",
                "Delay expansion and conduct thorough ethical review",
                "Explore alternative markets with fewer ethical concerns",
                "Engage local stakeholders to understand the situation better"
            ],
            "competencies": {
                "Strategic Thinking": [2, 3, 4, 5],
                "Ethical Leadership": [1, 5, 4, 3],
                "Risk Management": [1, 4, 3, 5]
            },
            "reasons": {
                "Strategic Thinking": [
                    "Prioritizes growth but overlooks potential risks",
                    "Balances growth with ethical considerations",
                    "Considers alternatives, showing adaptability",
                    "Demonstrates a holistic approach to decision-making"
                ],
                "Ethical Leadership": [
                    "Overlooks ethical concerns in favor of growth",
                    "Prioritizes ethical considerations highly",
                    "Considers ethics by seeking alternatives",
                    "Balances stakeholder interests with ethical concerns"
                ],
                "Risk Management": [
                    "Disregards potential risks in new market",
                    "Thoroughly assesses risks before proceeding",
                    "Mitigates risks by considering alternatives",
                    "Gathers information to make informed risk assessment"
                ]
            }
        },
        {
            "question": "A local official hints at expediting processes for a 'fee'. What's your response?",
            "choices": [
                "Pay the fee to speed up expansion",
                "Refuse and report the incident to authorities",
                "Seek advice from legal counsel before proceeding",
                "Attempt to negotiate a transparent, legal alternative"
            ],
            "competencies": {
                "Ethical Leadership": [1, 5, 4, 3],
                "Cross-Cultural Communication": [1, 2, 3, 5],
                "Risk Management": [1, 3, 4, 5]
            },
            "reasons": {
                "Ethical Leadership": [
                    "Compromises ethical standards for business advantage",
                    "Upholds highest ethical standards and legal compliance",
                    "Seeks guidance to ensure ethical compliance",
                    "Attempts to find ethical solution while maintaining relationships"
                ],
                "Cross-Cultural Communication": [
                    "Fails to consider cultural norms and legal implications",
                    "May damage relationships by not considering local practices",
                    "Seeks to understand legal and cultural context",
                    "Demonstrates cultural sensitivity while upholding ethics"
                ],
                "Risk Management": [
                    "Exposes company to legal and reputational risks",
                    "Mitigates immediate risk but may impact business operations",
                    "Carefully assesses risks before taking action",
                    "Balances risk mitigation with business continuity"
                ]
            }
        },
        {
            "question": "Your team is divided on the expansion. How do you proceed?",
            "choices": [
                "Make the final decision yourself based on available data",
                "Delay the decision until consensus is reached",
                "Conduct an anonymous vote among the leadership team",
                "Organize a structured debate to explore all perspectives"
            ],
            "competencies": {
                "Global Team Leadership": [2, 1, 3, 5],
                "Decision Making": [3, 1, 2, 5],
                "Adaptability": [2, 1, 3, 4]
            },
            "reasons": {
                "Global Team Leadership": [
                    "Shows decisiveness but may alienate team members",
                    "Avoids conflict but may lead to indecision",
                    "Involves team in decision-making process",
                    "Fosters open discussion and values diverse perspectives"
                ],
                "Decision Making": [
                    "Demonstrates decisive leadership but may overlook valuable input",
                    "Avoids making tough decisions, potentially harming business",
                    "Incorporates team input in decision-making process",
                    "Balances thorough analysis with timely decision-making"
                ],
                "Adaptability": [
                    "Rigidly adheres to hierarchical decision-making",
                    "Shows flexibility but may lead to missed opportunities",
                    "Adapts decision-making process to team dynamics",
                    "Demonstrates ability to adapt leadership style to situation"
                ]
            }
        },
        {
            "question": "Local market research reveals unexpected consumer preferences. How do you adapt?",
            "choices": [
                "Stick to the original product plan to maintain brand consistency",
                "Completely redesign products to match local preferences",
                "Create a localized product line alongside global offerings",
                "Conduct more in-depth research before making changes"
            ],
            "competencies": {
                "Adaptability": [1, 4, 5, 3],
                "Strategic Thinking": [2, 3, 5, 4],
                "Cross-Cultural Communication": [1, 3, 5, 4]
            },
            "reasons": {
                "Adaptability": [
                    "Lacks flexibility in response to market insights",
                    "Shows high adaptability but may overlook brand identity",
                    "Balances adaptability with maintaining global brand",
                    "Demonstrates cautious approach to adaptation"
                ],
                "Strategic Thinking": [
                    "Prioritizes global consistency over local opportunity",
                    "Reactive approach without considering long-term strategy",
                    "Strategically balances global and local considerations",
                    "Takes a measured approach to inform strategic decisions"
                ],
                "Cross-Cultural Communication": [
                    "Fails to consider local cultural preferences",
                    "Overemphasizes local preferences without global context",
                    "Effectively bridges global brand with local culture",
                    "Seeks to deepen understanding of local culture"
                ]
            }
        },
        {
            "question": "A global competitor announces expansion into the same market. Your response?",
            "choices": [
                "Accelerate your expansion plans to beat them to market",
                "Refocus on defending your existing markets instead",
                "Propose a joint venture to the competitor",
                "Differentiate your offering to target a specific niche"
            ],
            "competencies": {
                "Strategic Thinking": [3, 2, 4, 5],
                "Risk Management": [2, 3, 4, 5],
                "Adaptability": [4, 2, 3, 5]
            },
            "reasons": {
                "Strategic Thinking": [
                    "Shows aggressive strategy but may be hasty",
                    "Defensive strategy may miss growth opportunities",
                    "Creative approach to turn competition into opportunity",
                    "Demonstrates strategic differentiation in competitive market"
                ],
                "Risk Management": [
                    "Increases risk through aggressive, rapid expansion",
                    "Reduces immediate risk but may limit long-term growth",
                    "Shares risk through partnership, but introduces new complexities",
                    "Mitigates risk through focused, differentiated approach"
                ],
                "Adaptability": [
                    "Quickly adapts plans but may be too reactive",
                    "Shows limited adaptability to new competitive landscape",
                    "Demonstrates flexibility in approach to competition",
                    "Adapts strategy to find unique market position"
                ]
            }
        }
    ]
}

if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'show_results' not in st.session_state:
    st.session_state.show_results = False

def evaluate_answers():
    competency_scores = {
        "Strategic Thinking": 0,
        "Ethical Leadership": 0,
        "Risk Management": 0,
        "Global Team Leadership": 0,
        "Decision Making": 0,
        "Adaptability": 0,
        "Cross-Cultural Communication": 0
    }
    reasons = {comp: [] for comp in competency_scores}
    
    for i, question in enumerate(scenario["questions"]):
        if i in st.session_state.answers:
            answer = st.session_state.answers[i]
            for competency, scores in question["competencies"].items():
                score = scores[answer]
                competency_scores[competency] += score
                reasons[competency].append(f"Q{i+1}: {question['reasons'][competency][answer]} (Score: {score})")
    
    return competency_scores, reasons

def get_feedback(score):
    if score < 6:
        return "Needs improvement. Consider focusing more on this area in your decision-making process."
    elif score < 9:
        return "Good foundation. Continue to develop these skills across various situations."
    else:
        return "Excellent. You demonstrate strength in this area. Keep refining your approach as you face new challenges."

st.title("CEO Leadership Challenge")

st.header(scenario["title"])
st.write(scenario["description"])

if not st.session_state.show_results:
    for i, question in enumerate(scenario["questions"]):
        answer = st.radio(question["question"], question["choices"], key=f"q{i}")
        st.session_state.answers[i] = question["choices"].index(answer)

    if st.button("Submit Answers"):
        if len(st.session_state.answers) == len(scenario["questions"]):
            st.session_state.show_results = True
            st.experimental_rerun()
        else:
            st.error("Please answer all questions before submitting.")

else:
    st.header("Results")
    competency_scores, reasons = evaluate_answers()

    for competency, score in competency_scores.items():
        st.subheader(f"{competency}: {score}")
        st.write(get_feedback(score))
        st.write("Reasons:")
        for reason in reasons[competency]:
            st.write(f"- {reason}")
        st.write("")

    if st.button("Restart Challenge"):
        st.session_state.answers = {}
        st.session_state.show_results = False
        st.experimental_rerun()