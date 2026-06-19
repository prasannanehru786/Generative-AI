from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# --------------------------------------------------
# Model Path
# --------------------------------------------------
MODEL_PATH = r"./models/qwen2.5-1.5b"

print("=" * 60)
print("Loading Qwen Model...")
print("=" * 60)

# --------------------------------------------------
# Load Tokenizer
# --------------------------------------------------
tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH,
    trust_remote_code=True
)

# --------------------------------------------------
# Load Model
# --------------------------------------------------
model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    torch_dtype="auto",
    device_map="auto",
    low_cpu_mem_usage=True,
    trust_remote_code=True
)

print("\n✅ Model Loaded Successfully!")
print("💬 Qwen Chatbot Ready")
print("Type 'exit' or 'quit' to stop.\n")

# --------------------------------------------------
# Conversation History
# --------------------------------------------------
history = []

# --------------------------------------------------
# Chat Loop
# --------------------------------------------------
while True:

    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("\n👋 Goodbye!")
        break

    history.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    try:

        text = tokenizer.apply_chat_template(
            history,
            tokenize=False,
            add_generation_prompt=True
        )

        inputs = tokenizer(
            text,
            return_tensors="pt"
        ).to(model.device)

        print("\n🤖 Thinking...\n")

        with torch.no_grad():

            outputs = model.generate(
                **inputs,
                max_new_tokens=100,
                temperature=0.7,
                top_p=0.9,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id
            )

        response = tokenizer.decode(
            outputs[0][inputs.input_ids.shape[1]:],
            skip_special_tokens=True
        )

        history.append(
            {
                "role": "assistant",
                "content": response
            }
        )

        print(f"Qwen: {response}\n")

    except Exception as e:
        print(f"\n❌ Error: {e}\n")