from flask import Flask, render_template, Response
from datetime import datetime, timezone

app = Flask(__name__)

EVENT = {
    "title": "제 42회 등마루회장배",
    "host": "회장 신은",
    "date_text": "2025년 10월 22일 (수) 오전 10시",
    "place": "목동 운동장 테니스장",
    "desc": "등마루 가족이 뜻깊은 날에 더 빛날 수 있게 함께 해주세요.",
    # 캘린더 파일(ICS)용 시간 (KST 10:00 ≈ UTC 01:00)
    "start_dt": datetime(2025, 10, 22, 1, 0, 0, tzinfo=timezone.utc),
    "end_dt":   datetime(2025, 10, 22, 4, 0, 0, tzinfo=timezone.utc),
    # 스크롤 시 펼쳐질 편지 본문 (원하시는 텍스트로 바꿔 넣으세요)
    "letter": """

제 42회 등마루회장배에 초대합니다.

매주 함께 행복하고, 매년 함께 성장하며
55인의 등마루인들이 우리의 멋진 팀을 만들어가고 있습니다.

작은 더 커다란 기쁨이 자연스런 일이 되는 날에
웃음으로 소중한 시간을 함께 하고자 초대장을 전합니다.

2025년 10월 22일 수요일 오전 10시
목동 운동장 테니스장
"""
}

@app.route("/")
def index():
    return render_template("index.html", event=EVENT)

@app.route("/event.ics")
def event_ics():
    """캘린더 추가 파일 다운로드"""
    uid = "deungmaru-42@invite"
    dtstart = EVENT["start_dt"].strftime("%Y%m%dT%H%M%SZ")
    dtend   = EVENT["end_dt"].strftime("%Y%m%dT%H%M%SZ")
    ics = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Deungmaru Invite//KR
CALSCALE:GREGORIAN
BEGIN:VEVENT
UID:{uid}
SUMMARY:{EVENT['title']}
DESCRIPTION:{EVENT['desc']}
DTSTART:{dtstart}
DTEND:{dtend}
LOCATION:{EVENT['place']}
END:VEVENT
END:VCALENDAR
"""
    return Response(ics, mimetype="text/calendar")

if __name__ == "__main__":
    # macOS에서 5000 충돌 시 5001 사용
    app.run(host="0.0.0.0", port=5001)
