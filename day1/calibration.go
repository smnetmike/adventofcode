package main

import (
	"os"
	"bufio"
	"strconv"
	"log"
	"fmt"
)

func main() {

	visitedFrequency := make(map[int]bool)
	currentFreq := 0
	visitedFrequency[currentFreq] = true
	readFile := true
	for readFile {
		
		file, err := os.Open("input.txt")
		if err != nil {
			log.Fatal(err)
		}

		scanner := bufio.NewScanner(file)
		for scanner.Scan() {
			val, err := strconv.Atoi(scanner.Text())
			if err != nil {
				log.Fatal(err)
			}
			currentFreq += val
			if visitedFrequency[currentFreq] {
				fmt.Printf("First revisited frequency: %d\n", currentFreq)
				readFile = false
				break
			} else {
				visitedFrequency[currentFreq] = true
			}

			if err := scanner.Err(); err != nil {
				log.Fatal(err)
			}

		}

		file.Close()
	}

}
