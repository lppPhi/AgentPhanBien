from gemini import call_gemini

def debater_a(topic: str, rebuttal: str = ""):
    prompt = f"Bạn là Người tranh luận A ủng hộ chủ đề: '{topic}'."
    if rebuttal:
        prompt += f"\nPhản bác lập luận của người tranh luận B: {rebuttal}"
    return call_gemini(prompt)

def debater_b(topic: str, rebuttal: str = ""):
    prompt = f"Bạn là Người tranh luận B phản đối chủ đề: '{topic}'."
    if rebuttal:
        prompt += f"\nPhản bác lập luận của người tranh luận A: {rebuttal}"
    return call_gemini(prompt)

def judge(debate_log: str):
    prompt = (
    "Bạn là trọng tài trong một cuộc tranh luận giữa hai người về chủ đề dưới đây. "
    "Dựa trên các lập luận được trình bày, hãy thực hiện các bước sau:\n\n"
    "1. Phân tích từng lập luận của mỗi bên dựa trên các tiêu chí:\n"
    "   - Tính logic và mạch lạc\n"
    "   - Tính thuyết phục và chiều sâu lập luận\n"
    "   - Sự hỗ trợ bằng ví dụ, dữ kiện, hoặc lập luận thực tế\n"
    "   - Khả năng phản biện và làm rõ điểm yếu của đối phương\n\n"
    "2. Đưa ra kết luận ai là người tranh luận thuyết phục hơn.\n"
    "3. Giải thích lý do chọn người chiến thắng bằng một đoạn văn ngắn, rõ ràng và công bằng.\n\n"
    f"Dưới đây là toàn bộ nội dung cuộc tranh luận:\n\n{debate_log}"
)

    return call_gemini(prompt)
