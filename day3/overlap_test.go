package main

import (
	"testing"
	"reflect"
)

func TestOverlap(t *testing.T) {
	cases := []struct{
		line string
		clID string
		topLeft Point
		width string
		height string
	}{
		{"#1 @ 258,327: 19x22", "1", Point{258, 327}, "19", "22"},
	}
	for _, c := range cases {

		clID, topLeft, width, height := parseLine(c.line)
		if clID != c.clID || !reflect.DeepEqual(topLeft, c.topLeft) || width != c.width || height != c.height {
			t.Errorf("parseLine(%q) = (%+v, %q, %q) want (%+v, %q, %q)", c.line, topLeft, width, height, 
			c.topLeft, c.width, c.height)
		}

	}
}