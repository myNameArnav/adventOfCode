package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func maxInArray(caloriesArr []int) int {

	max := caloriesArr[0]

	for i := 0; i < len(caloriesArr); i++ {
		if caloriesArr[i] > max {
			max = caloriesArr[i]
		}
	}
	// fmt.Println("hello")
	return max
}

func topTwo(caloriesArr []int) int {
	// smaller than the maximum * 3

	topTwo := caloriesArr[0]

	for i := 0; i < len(caloriesArr); i++ {
		if caloriesArr[i] > topTwo && caloriesArr[i] < maxInArray(caloriesArr) {
			topTwo = caloriesArr[i]
		}
	}

	return topTwo
}

func topThree(caloriesArr []int) int {
	// smaller than the maximum * 3

	topThree := caloriesArr[0]

	for i := 0; i < len(caloriesArr); i++ {
		if caloriesArr[i] > topThree && caloriesArr[i] < topTwo(caloriesArr) {
			topThree = caloriesArr[i]
		}
	}

	return topThree
}

func main() {
	f, err := os.Open("2022/Day1/input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)

	calorie := 0
	totalCalorie := 0
	caloriesArr := []int{}

	for scanner.Scan() {
		newLine := scanner.Text()

		if newLine != "" {
			calorie, err = strconv.Atoi(newLine)
		} else {
			calorie = 0
		}

		if err != nil {
			log.Fatal(err)
		}

		if calorie == 0 {
			caloriesArr = append(caloriesArr, totalCalorie)
			totalCalorie, calorie = 0, 0
		} else {
			totalCalorie += calorie
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	max := maxInArray(caloriesArr)
	topTwo := topTwo(caloriesArr)
	topThree := topThree(caloriesArr)

	sum := max + topTwo + topThree

	fmt.Println("Max is :", max)

	fmt.Println("Sum of top three is: ", sum)
}
