from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

    print("Olutvarasto lopuksi:")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")


if __name__ == "__main__":
    main()
