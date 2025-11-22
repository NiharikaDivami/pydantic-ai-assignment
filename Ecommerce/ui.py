from fasthtml.common import fast_app, Script, H1, P, Form, Input, Button, Div, Span
from fasthtml.fastapp import serve

app, routes = fast_app(
    title="Ecommerce UI",
    htrs=(
        Script(src="https://cdn.tailwindcss.com", pico=False),
    )

)

@routes("/")
def home():
    return Div(
        H1("Welcome to the Ecommerce UI", _class="text-4xl font-bold text-center text-blue-700 mb-6"),
        P("This is the home page of the Ecommerce application.", _class="text-lg text-center text-gray-600 mb-8"),
        Form(
            Input(type="text", name="query", placeholder="Enter your query...", _class="border border-gray-300 rounded-lg px-4 py-2 w-full mb-4 focus:outline-none focus:ring-2 focus:ring-blue-400"),
            Button("Send", type="submit", _class="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-6 rounded shadow transition duration-300"),
            hx_post="/send",
            hx_target="#response",
            hx_swap="beforeend",
            _class="flex flex-col items-center"
        ),
        Div(id="response", _class="mt-6 flex flex-col gap-4"),
        _class="max-w-xl mx-auto bg-white p-10 rounded-xl shadow-2xl mt-20 min-h-screen flex flex-col justify-center"
    )


@routes("/send")
def send(query: str):
    # User message bubble (right aligned)
    user_msg = Div(
        Span(query, _class="block"),
        _class="bg-blue-500 text-white rounded-2xl px-4 py-2 max-w-xs ml-auto shadow-md text-right mb-2 flex flex-row-reverse items-end"
    )
    # Bot/response message bubble (left aligned, example static response)
    bot_response = Div(
        Span("Thank you for your message!", _class="block"),
        _class="bg-gray-200 text-gray-800 rounded-2xl px-4 py-2 max-w-xs mr-auto shadow-md text-left mb-2 flex items-end"
    )
    return user_msg + bot_response


serve(port=1010)