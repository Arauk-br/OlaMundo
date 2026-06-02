#!/usr/bin/env python3
"""Runner simples para o projeto OlaMundo."""

import argparse


def main(name: str):
    print(f"Olá, {name}!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OlaMundo runner")
    parser.add_argument("--name", "-n", default="Mundo", help="Nome para cumprimentar")
    args = parser.parse_args()
    main(args.name)
