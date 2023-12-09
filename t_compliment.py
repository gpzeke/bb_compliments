from compliment_data_management import ComplimentData

def main():
    compliment_manager = ComplimentData()
    compliment = compliment_manager.random_compliment()
    print(compliment)

if __name__ == "__main__":
    main()