package main

/*
Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}

You can assume keys do not contain dots in them, i.e. no clobbering will occur.
*/

import "fmt"

func flatten(dict map[string]interface{}) map[string]interface{} {
	for key, value := range dict {
		if value, ok := value.(map[string]interface{}); ok {
			for k, v := range flatten(value) {
				dict[key+"."+k] = v
			}
			delete(dict, key)
		}
	}

	return dict
}

func main() {
	dict := map[string]interface{}{
		"key": 3,
		"foo": map[string]interface{}{
			"a": 5,
			"bar": map[string]interface{}{
				"baz": 8,
			},
		},
	}

	fmt.Println("dict =", dict)
	fmt.Printf("flatten(dict) = %v", flatten(dict))
}
