import os
import openai


openai.api_key = os.environ.get('API_KEY')


SYSTEM_MESSAGE = "You are a Python Tutor AI, dedicated to helping users learn Python and build end-to-end projects using Python and its related libraries. Provide clear explanations of Python concepts, syntax, and best practices. Guide users through the process of creating projects, from the initial planning and design stages to implementation and testing. Offer tailored support and resources, ensuring users gain in-depth knowledge and practical experience in working with Python and its ecosystem."


def completion(prompt, **kwargs):
    return openai.ChatCompletion.create(
        **kwargs,
        model="gpt-3.5-turbo",
        messages=[
            {
                'role': 'system',
                'content': SYSTEM_MESSAGE
            },
            {
                'role': 'user',
                'content': prompt
            }
        ],
    )
