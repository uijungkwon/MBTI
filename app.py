import os

from dash import Dash, dcc, html

from callbacks import get_callbacks
from utils import MBTI

app = Dash(__name__)
server = app.server

def user_controls(): #사용자로부터 조작을 입력받음
    return html.Div(

        [  
            html.Label("이름"),
            dcc.Input(placeholder = "블랙핑크", type="text", id = "name-input"),
            html.Label("나이"),
            dcc.Input(placeholder = "20", type="number", id = "age-input"),
            html.Label("MBTI"),
            dcc.Dropdown(options=MBTI,id = "mbti-input"),
            html.Label("아바타 재생성"),
            html.Button("재생성", id = "avatar-button", style = {
                    "font-size": "16px"
            }),
        ],
        className="three columns div-user-controls",
    )


def profile(): # 프로필 생성 
    return html.Div(
        [ html.Div([
            html.H2(
                "profile", style={
                    "font-size": "36px"}),
            
            html.Div([
                html.H2("이름",id = "name"),
                html.H2("나이", id = "age"),

            ]),
            html.Img(id = "avartar")
          ]
        ),
        html.H2("MBTI", style={"font-size": "36px"}),
        dcc.Graph(id = "mbti")
        ],
        className="nine columns bg-grey",
        style={
            "display": "flex",
            "flex-direction": "column",
            "flex-grow": 1,
        },
    )


app.layout = html.Div(
    children=[
        html.Div(
            className="row",
            children=[
                user_controls(),
                profile(),
            ],
        )
    ]
)

get_callbacks(app)

# Remove all svg files is assets folder --아바타 재생성 할 때마다 새로운 파일이 생겨 지우도록 코드 생성
for file in os.listdir("assets"):
    if file.endswith(".svg"):
        os.remove(os.path.join("assets", file))


if __name__ == "__main__":
    app.run_server()
