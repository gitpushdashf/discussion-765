from time import time, sleep
from typing import Iterator

from flask import Flask, Response


def main() -> None:
    app = Flask("Testing server")

    last_started = int(time())
    @app.route("/reload", methods=["GET"])
    def reload() -> Response:
        def stream() -> Iterator[str]:
            # When this is reloaded, it will actually break the connection.
            while True:
                yield f"data: {last_started}\n\n"
                sleep(1)  # pragma: nocover

        return Response(stream(), mimetype="text/event-stream")

    app.run(host="127.0.0.1", port=3001, use_reloader=True)


if __name__ == "__main__":
    main()
