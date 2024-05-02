# Vacancy Management System

This project provides a Vacancy Management System that allows users to interact with vacancies from the HeadHunter API and manage them using the `JsonSaver` class.

## HeadHunterAPI

The `HeadHunterAPI` class provides methods to interact with the HeadHunter API and retrieve vacancy data in JSON format.

## Vacancy

The `Vacancy` class includes methods to cast JSON data into a list of `Vacancy` objects, making it easier to work with vacancy data.

## JsonSaver

The `JsonSaver` class is responsible for managing vacancies using a JSON file as the storage medium. It provides the following functions:

### `load_vacancies(self)`

This function loads vacancies from the "vacancies.json" file. If the file is not found or if there is a JSON decoding error, it initializes the vacancies list as empty.

### `add_vacancy(self, vacancy)`

This function adds a new vacancy to the system. It creates a dictionary containing the vacancy details and appends it to the vacancies list. It then updates the "vacancies.json" file with the new vacancy data.

### `get_vacancies(self, id)`

This function retrieves a specific vacancy based on its ID from the vacancies list.

### `remove_vacancy(self, vacancy_id)`

This function removes a vacancy from the system based on its ID. It iterates through the vacancies list, finds the matching vacancy, removes it, and updates the "vacancies.json" file.

### Example
```python
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies("Python", count=3)
    vaca = Vacancy.cast_to_object_list(json_data=hh_vacancies)  

    vacancy = Vacancy("Python Developer", URL="https://hh.tu/1231451512", salary="null", description="need to super power")
    vacancy2 = Vacancy("Java Developer", URL="https://hh.tu/1231451512", salary="null", description="need to super power")

    saver = JsonSaver()
    saver.add_vacancy(vacancy)
    saver.add_vacancy(vacancy)
    saver.add_vacancy(vacancy2)
    data = saver.get_vacancies(1)
    saver.remove_vacancy(0)
```

## UserClient

The `UserClient` function provides a user interface for interacting with the HeadHunter API and managing vacancies using the `JsonSaver` class. It allows users to input search queries, retrieve and display vacancies, and perform keyword-based searches on vacancy descriptions.

For detailed usage and examples, refer to the code documentation and examples provided in the project.