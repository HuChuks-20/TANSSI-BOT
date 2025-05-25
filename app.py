""" from flask import Flask, render_template, request
from flask_cors import CORS
import difflib

app = Flask(__name__)
CORS(app)

qa_pairs = {
    "hey":"Yoo! ready to  launch faster,scale smarter and vibe harder? just say the word!",
    "hello":"heya!it's forkie here-sharp,shiny,and ready to  serve some mainnet magic.what can i help you with today?",
    "hi":"hey hey,friend!forkie here-your favourite dancing fork and tanssi official sidekick-Need help launchung an appchain?want the scoop on maiinet?or just here to  vibe and build ?i got you ",
    "what is tanssi":"Tanssi is a framework for launching appchains fast, with infra like RPC and wallet integration.Tanssi abstracts the infrastructure layer—validator orchestration, sequencing, and tooling—so teams can launch with real security and full control. Whether you’re building an AVS, appchain, or custom network, Tanssi gives you the freedom to focus on logic, not low-level coordination.",
    "who is forkie": "Forkie is Tanssi’s mascot — your appchain tour guide.",
    "how does tanssi help": "Tanssi makes launching appchains easier with no-code tools and shared security from Polkadot.",
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def chatbot():
    msg = request.args.get("msg", "").lower()

    # Find closest match using fuzzy matching
    best_match = difflib.get_close_matches(msg, qa_pairs.keys(), n=1, cutoff=0.4)

    if best_match:
        return qa_pairs[best_match[0]]
    else:
        return "🤖 I’m not sure how to answer that yet. Try asking about Tanssi, Forkie, or appchains."

if __name__ == "__main__":
    app.run(debug=True)"""





from flask import Flask, render_template, request
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

# Keyword-based smart Q&A
qa_keywords = {
     "hi":"hey hey,friend!forkie here-your favourite dancing fork and tanssi official sidekick-Need help launchung an appchain?want the scoop on maiinet?or just here to  vibe and build ?i got you ",
    "hey":"Yoo! ready to  launch faster,scale smarter and vibe harder? just say the word!",
    "hello":"heya!it's forkie here-sharp,shiny,and ready to  serve some mainnet magic.what can i help you with today?",
    "tanssi": "Tanssi is a launchpad for appchains built on Polkadot. It helps developers launch their own blockchain with minimal setup.Tanssi abstracts the infrastructure layer—validator orchestration, sequencing, and tooling—so teams can launch with real security and full control. Whether you’re building an AVS, appchain, or custom network, Tanssi gives you the freedom to focus on logic, not low-level coordination.",
    "forkie": "Forkie is the Tanssi mascot — fast, creative, and always on-chain!",
    "rpc": "Tanssi provides fast and scalable RPC endpoints for appchains to connect and interact efficiently.",
    "explorer": "Tanssi includes chain explorers so you can easily monitor appchain transactions and activity.",
    "wallet": "Tanssi integrates wallets for users to interact with appchains easily.",
    "launch": "You can launch an appchain on Tanssi in minutes using its modular tools and shared infrastructure.",
    "infrastructure": "Tanssi provides modular infrastructure like shared security, RPCs, and tooling to make launching an appchain easy.",
    "shared security": "Appchains on Tanssi benefit from Polkadot’s shared security model — so you don’t have to bootstrap your own.",
    "tooling": "Tanssi offers CLI tools, templates, and dashboards to help you build and deploy appchains fast.",
    "appchain": "An appchain is a blockchain built for a specific app — Tanssi makes launching them seamless.",
    "mainnet":"tanssi mainnet and TGE is scheduled for june 2025(no exact date yet).",
     "campaign":"Journey to Mainnet, Tanssi's Pre-TGE Airdrop Campaign is Live on DISCORD ,GALXE AND GUILD ",
   "builders":"cycle,everclear,particle,symbiotic.you c", # type: ignore
   "contribute":"""first, you need roles.Now that you have your role — here’s how to start contributing and growing🔹 Step 1: Create Your Activity Tracker Post
- Go to tanssi discord -activity tracker
- Create a post titled: [YourUsername] - Activity Log
- Log everything you contribute (threads, content, support, events)
- Add proof: links, screenshots, or details

🔹 *Step 2: Start Contributing*
Focus on what you do best:
- ✍ Threads, articles, memes, videos, designs
- 🧠 Quizzes, translations, community support
- 🤝 Outreach to KOLs, projects, builders

💬 Quality > Quantity. Focus on real value, creativity, and Tanssi’s mission.

🔹 *Step 3: Grow Your Impact*
- Earn 💎 Coco Gems for consistent contributions
- Earn 🎟 Forkie Tickets for standout work
- Unlock bigger roles and perks over time!
""""",
    "roles":""""🔹 *[Apply to Journey to Mainnet](https://app.galxe.com/quest/tanssinetwork/GCLVrtmwM5)* by completing *[Galxe Q1](<https://app.galxe.com/quest/tanssinetwork/GCLVrtmwM5>)*— a quick survey to get started
🔹 Dancer L2 → 3,500 Coco Gems + 1 Forkie Ticket + Active contributions
🔹 Dancer L3 → 5,000 Coco Gems + 2 Forkie Tickets + Recognized impact
🔹 Forkstar → 10,000 Coco Gems + 3 Forkie Tickets + Proven leadership

*Skill-Based Roles*
(Creatooor, Memooor, etc.):  → 3,000 Coco Gems + 1 Forkie Ticket + Proof of work

*Community Mod*
- 7,000 Coco Gems + History of helping and good vibes
""",
  "link":"discordlink(https://discord.gg/tanssi),galxe link(https://app.galxe.com/quest/tanssinetwork/GCLVrtmwM5) ,guild(guild.xyz/tanssinetwork)",
       
  "tge":"""TGE and mainnet is scheduled for Q2(june) 2025- more details on $TANSSI distribution;core community& ecosystem programs(30% unlocks at TGE,with  the rest distributed through monthly unlocking for three years-Note:some sub programs like JTM are fully unlocked @ TGE),
     community sales(fully unlocked 40 days post TGE), LFD campaigns(20% unlocks at TGE, with the remaining 80% unlocking over 60 days),
    Foundation reserve(30% unlocks at TGE, and the remaining 70%  unlocks monthly for three years).
""",
   "started":"""hey! to  get started, join our discord server .link(https://discord.gg/tanssi) go to -activity tracker
- Create a post titled: [YourUsername] - Activity Log
- Log everything you contribute (threads, content, support, events)
- Add proof: links, screenshots, or details"""""
}
   

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def chatbot():
    user_msg = request.args.get("msg", "").lower()
    for keyword, answer in qa_keywords.items():
        if re.search(rf"\b{keyword}\b", user_msg):
            return answer
    return "🤖 Hmm... I’m not sure about that. Try asking something about Tanssi, Forkie, RPCs, or appchains."

if __name__ == "__main__":
    app.run(debug=True)
