import plotly.express as px
from dash.dependencies import Input, Output
from plotly import graph_objects as go

from utils import MBTI, random_avatar


def get_callbacks(app): # 콜백 함수 작성 

    @app.callback(
        Output("avartar", "src"),
        Input("avartar-button", "n-clicks"),
    )
    def update_avatar(clicks):
        return random_avatar 
    @app.callback(
        Output("mbti","figure"),
        Input("mbti-input", "value")
    )
    def update_pie_lchart(mbti):
        color = px.colors.diverging.RdBu # 선택 되었을 때 mbti 표시함
        if mbti is not None: #mbti가 선택되지 않았을 때 mbti색깔 표시
            color = [
                "#FF1010" if mbti == m else "#323130"
                for m in MBTI
            ]
        pie_chart = go.figure(
            go.Pie(
                values=[1]*16, 
                labels=MBTI,
                textinfo = "label", 
                hoverinfo = "label", 
                hole =0.6,
                textfont= {"size":20},
                marker = dict(colors = px.colors.diverging.RdBu)
            )
        )
        pie_chart.update_layout(
            margin=dict(l = 0, r = 0, t = 0, b = 0),
            showlegend = False,
            paper_bgcolor = "#323130"
        )

        return pie_chart
    @app.callback(
        Output("mbti-input", "value"),
        Input("mbti", "clickData"),
    )
    def update_mbti_input_from_pie_chart(mbti):
        if mbti is None:
            return None # mbti가 선택되지 않았을 때 아무것도 출력하지 않도록 지정함
        return mbti["points"][0]["label"]
    @app.callback(
        Output("name", "children"), Input("name-input")
)
    def update_name(name):
        if name is None:
            return "이름"
        return f"이름{name}"
    def update_name(age):
        if age is None:
            return "나이"
        return f"나이{age}"