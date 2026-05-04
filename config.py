
# ==========================================
# Future-Grow-AI-Master Comprehensive Config
# ==========================================

# ১. Google Gemini AI Settings
# আপনি এখান থেকে কী পাবেন: https://aistudio.google.com/app/apikey
GEMINI_API_KEYS = [
    "এখানে_আপনার_প্রথম_জেমিনি_কী_দিন",
        "এখানে_আপনার_দ্বিতীয়_জেমিনি_কী_দিন"
        ]

        # ২. Groq AI Settings (অতি দ্রুত গতির জন্য)
        # আপনি এখান থেকে কী পাবেন: https://console.groq.com/keys
        GROQ_API_KEYS = [
            "এখানে_আপনার_গ্রোক_কী_দিন"
            ]

            # ৩. Hugging Face Settings (ফেস রিকগনিশন ও অন্যান্য এআই মডেল)
            # আপনি এখান থেকে কী পাবেন: https://huggingface.co/settings/tokens
            HF_TOKEN = "এখানে_আপনার_হাগিং_ফেস_টোকেন_দিন"

            # ৪. OpenAI Settings (যদি ভবিষ্যতে ব্যবহার করতে চান)
            OPENAI_API_KEY = "এখানে_আপনার_ওপেন_এআই_কী_দিন"

            # ৫. ডিফল্ট মডেল সিলেকশন
            ACTIVE_GEMINI_MODEL = "gemini-1.5-flash"
            ACTIVE_GROQ_MODEL   = "llama3-70b-8192"
            ACTIVE_HF_MODEL     = "mistralai/Mistral-7B-v0.1"

            # ৬. সিস্টেম সেটিংস
            TEMPERATURE = 0.7
            MAX_TOKENS = 2048
            DEBUG_MODE = True

            print("All AI Keys and Configurations have been loaded safely!")
