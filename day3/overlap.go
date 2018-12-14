package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Point struct {
	X, Y int
}

type Claim struct {
	topLeft Point
	width   int
	height  int
}

func parseLine(line string) (string, Point, string, string) {
	parts := strings.Split(line, " ")

	tmpArr := strings.Split(parts[0], "#")
	clID := tmpArr[1]

	tmp := strings.Split(parts[2], ":")
	tmp = strings.Split(tmp[0], ",")
	x, _ := strconv.Atoi(tmp[0])
	y, _ := strconv.Atoi(tmp[1])
	topLeft := Point{x, y}

	tmp = strings.Split(parts[3], "x")
	width := tmp[0]
	height := tmp[1]

	return clID, topLeft, width, height
}

func main() {

	nbSharedPoints := 0
	nbPoints := 0

	mapPointToOcc := make(map[Point]int)
	claims := make(map[int]Claim, 0)
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		clID, topLeft, width, height := parseLine(scanner.Text())
		clid, _ := strconv.Atoi(clID)
		wd, _ := strconv.Atoi(width)
		hght, _ := strconv.Atoi(height)
		claims[clid] = Claim{topLeft, wd, hght}
		for i := 1; i <= wd; i++ {
			for j := 1; j <= hght; j++ {
				currPoint := Point{topLeft.X + i, topLeft.Y + j}
				if currPoint.X > 1000 || currPoint.Y > 1000 {
					continue
				}
				if _, ok := mapPointToOcc[currPoint]; !ok {
					mapPointToOcc[currPoint] = 1
				} else {
					mapPointToOcc[currPoint]++
				}
			}
		}
	}

	for _, v := range mapPointToOcc {
		if v > 1 {
			nbSharedPoints++
		}
		nbPoints++
	}

	var noOverlapClaimID int
	var noOverlap bool

	// Checking claims
	for id, cl := range claims {
		noOverlap = true
		for i := 1; i <= cl.width; i++ {
			if !noOverlap {
				break
			}
			for j := 1; j <= cl.height; j++ {
				currPoint := Point{cl.topLeft.X + i, cl.topLeft.Y + j}
				if mapPointToOcc[currPoint] > 1 {
					noOverlap = false
					break
				}
			}
		}
		if noOverlap {
			noOverlapClaimID = id
			break
		}
	}

	fmt.Println("Number of points: ", nbPoints)
	fmt.Println("Number of common points: ", nbSharedPoints)
	fmt.Println("No Overlap claim: ", noOverlapClaimID)

}
