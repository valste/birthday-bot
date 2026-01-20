import asyncio
import argparse
from bot.config import get_settings
from bot.logging import setup_logging


async def run_once() -> None:
    settings = get_settings()
    _ = settings  # Wire services and run generation
    setup_logging()
    # TODO: implement orchestration


def main() -> None:
    parser = argparse.ArgumentParser(description="Birthday bot runner")
    parser.add_argument("--schedule", action="store_true", help="Run scheduler")
    parser.add_argument("--once", action="store_true", help="Run once immediately")
    args = parser.parse_args()

    if args.schedule:
        from bot.scheduler import start_scheduler

        def job():
            asyncio.run(run_once())

        start_scheduler(job)
        try:
            import time

            while True:
                time.sleep(60)
        except KeyboardInterrupt:
            return
    else:
        asyncio.run(run_once())


if __name__ == "__main__":
    main()
