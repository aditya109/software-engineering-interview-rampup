package main

import "fmt"

func permutation(str string) []string {
	var result []string
	permute([]rune(str), 0, &result)
	return result
}

func permute(s []rune, start int, result *[]string) {
	if start == len(s)-1 {
		*result = append(*result, string(s))
		return
	}
	for i := start; i < len(s); i++ {
		s[start], s[i] = s[i], s[start]
		permute(s, start+1, result)
		s[start], s[i] = s[i], s[start]
	}
}

func main() {
	str := "ARAM"
	perms := permutation(str)
	fmt.Println(perms)
}
