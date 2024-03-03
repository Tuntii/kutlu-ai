import replicate
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

async def text_to_photo(prompt : str):
    output = replicate.run(
        "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
        input={"prompt": prompt }
        )
    
    return output[0]

async def text_to_video(prompt : str):
    # output = replicate.run(
    #     "stability-ai/stable-video-diffusion:3f0457e4619daac51203dedb472816fd4af51f3149fa7a9e0b5ffcf1b8172438",
    #     input={"prompt": prompt}
    #     )
    output = replicate.run(
    "stability-ai/stable-video-diffusion:3f0457e4619daac51203dedb472816fd4af51f3149fa7a9e0b5ffcf1b8172438",
    input={
        "cond_aug": 0.02,
        "decoding_t": 7,
        "input_image": await text_to_photo(prompt=prompt),
        "video_length": "14_frames_with_svd",
        "sizing_strategy": "maintain_aspect_ratio",
        "motion_bucket_id": 127,
        "frames_per_second": 6
    })
    return output
# stability-ai/stable-video-diffusion:3f0457e4619daac51203dedb472816fd4af51f3149fa7a9e0b5ffcf1b8172438

async def text_to_text(prompt: str):
    output = replicate.run(
        "01-ai/yi-34b-chat:914692bbe8a8e2b91a4e44203e70d170c9c5ccc1359b283c84b0ec8d47819a46",
    input={
            "top_k": 50,
            "top_p": 0.8,
            "prompt": prompt,
            "temperature": 0.3,
            "max_new_tokens": 1024,
            "prompt_template": "<|im_start|>system\nYou are a helpful assistant<|im_end|>\n<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n",
            "repetition_penalty": 1.2
        }
    )
    return output
