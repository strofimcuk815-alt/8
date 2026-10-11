def process_list(input_list):
    try:
        assert len(input_list) >= 3, "Список повинен містити принаймні 3 елементи"
        print(f"Список містить {len(input_list)} елементів")
    except AssertionError as e:
        print(e)
process_list([10, 20, 30, 40])
process_list([1, 2])