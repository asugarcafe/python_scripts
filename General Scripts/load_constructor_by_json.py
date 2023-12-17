# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 20:05:55 2023

@author: sucre
"""
import json

class CustomClass1:
    def __init__(self, prop1):
        self.prop1 = prop1

    def __repr__(self):
        return f"CustomClass1(prop1={self.prop1})"

class CustomClass2:
    def __init__(self, prop2):
        self.prop2 = prop2

    def __repr__(self):
        return f"CustomClass2(prop2={self.prop2})"

class MyClass:
    def __init__(self, json_str):
        data = json.loads(json_str)

        # Set the properties from the JSON data
        self.property1 = data.get('property1', None)
        self.property2 = data.get('property2', None)
        self.property3 = data.get('property3', None)
        self.property4 = data.get('property4', None)
        self.property5 = data.get('property5', None)

        # Custom classes properties
        custom1_data = data.get('custom1', {})
        self.custom1 = CustomClass1(custom1_data.get('prop1', None))

        custom2_data = data.get('custom2', {})
        self.custom2 = CustomClass2(custom2_data.get('prop2', None))

    def __repr__(self):
        return (
            f"MyClass(property1={self.property1}, property2={self.property2}, "
            f"property3={self.property3}, property4={self.property4}, "
            f"property5={self.property5}, custom1={self.custom1}, custom2={self.custom2})"
        )

# Example usage:
if __name__ == "__main__":
    json_str = '{"property1": "value1", "property2": "value2", "property3": "value3", ' \
               '"property4": "value4", "property5": "value5", ' \
               '"custom1": {"prop1": "custom_value1"}, ' \
               '"custom2": {"prop2": "custom_value2"}}'

    my_instance = MyClass(json_str)
    print(my_instance)
