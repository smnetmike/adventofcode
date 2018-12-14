package main

import (
	"os"
	"bufio"
	"strings"
	"log"
	"fmt"
)

func calculateChecksum() int {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var twoLettersCount, threeLettersCount int
	scanner := bufio.NewScanner(file)
	// nbLines := 1
	// nbLinesDebug := 2
	for scanner.Scan() {
		letterToCountMap := make(map[string]int)
		strArr := strings.Split(scanner.Text(), "")
		for _, str := range strArr {
			if _, ok := letterToCountMap[str]; !ok {
				letterToCountMap[str] = 1
			} else {
				letterToCountMap[str]++
			}
		}
		// log.Println(strArr)
		// log.Println(letterToCountMap)
		first2Letter := true
		first3Letter := true
		for _, v := range letterToCountMap {
			if first2Letter && v == 2 {
				twoLettersCount++
				first2Letter = false
			}
			if first3Letter && v == 3 {
				threeLettersCount++
				first3Letter = false
			}
		}
		// log.Println("twoLettersCount: ", twoLettersCount)
		// log.Println("threeLettersCount: ", threeLettersCount)
		
		/* if nbLines == nbLinesDebug {
			break
		}
		nbLines++ */
	}
	checksum := twoLettersCount * threeLettersCount
	return checksum
}

func storeFileToArray() []string {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	strArr := make([]string, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		strArr = append(strArr, scanner.Text())
	}
	return strArr
}

func findClosestStringCommonPart(strArr []string) string {

	for i, str := range strArr {
		for j := i + 1; j < len(strArr); j++ {
			compStr := strArr[j]
			strLen := len(str)
			nbDiff := 0
			diffInd := 0
			for c := 0; c < strLen; c++ {
				if str[c] != compStr[c] {
					nbDiff++
					diffInd = c
				}
				if (nbDiff > 1) {
					break
				}
			}
			if (nbDiff == 1) {
				fmt.Println("strings are: ", str, "and ", compStr)
				return strings.Replace(str, string(str[diffInd]), "", 1)
			}
		}
	}
	return ""
}

func main() {

	/* checksum := calculateChecksum()
	fmt.Printf("Checksum is: %d \n", checksum) */

	strArr := storeFileToArray()
	commonPart := findClosestStringCommonPart(strArr)
	fmt.Printf("Common part: %s \n", commonPart)

}