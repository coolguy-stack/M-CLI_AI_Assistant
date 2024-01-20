import { config } from "dotenv";
import readline from "readline";
import { OpenAI } from "openai";

config();

const openai = new OpenAI({
    apiKey: process.env.API_KEY
});

const userInterface = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const conversationHistory = [];

function getUserInput() {
    userInterface.question("You: ", (userMessage) => {
        if (userMessage.toLowerCase() === 'exit') {
            userInterface.close();
            return;
        }

        conversationHistory.push({ role: "user", content: userMessage });

        openai.chat.completions.create({
            model: "gpt-3.5-turbo",
            messages: conversationHistory
        }).then((res) => {
            const aiResponse = res.choices[0].message.content;
            console.log("M: " + aiResponse);

            conversationHistory.push({ role: "assistant", content: aiResponse });

            getUserInput();
        }).catch((error) => {
            console.error("Error:", error);
            getUserInput();
        });
    });
}

console.log("Welcome! Let's chat. Type 'exit' to end the conversation.");
conversationHistory.push({ role: "assistant", content: "Hello! I am M, your personal CLI AI Assistant!." });

getUserInput();
