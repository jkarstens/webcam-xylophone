// getXyloNoteOnAt.js
// If movement is detected at the indexth xylo note, output the index.
// Otherwise, output -1.
// DELTA_THRESHOLD controls how sensitive the algorithm is to movement.

inlets = 2;
outlets = 1;
var index = jsarguments[1];
var DELTA_THRESHOLD = 200;

function jit_matrix(in_matrix) {		
	var matrix = new JitterMatrix(in_matrix);
	var BAR_WIDTH = Math.floor(matrix.dim[0] / 8);
	// post(matrix.getcell(0, 0) + "\n");
	for (var x = index * BAR_WIDTH; x < (index + 1) * BAR_WIDTH; x++) {
		for (var y = 0; y < matrix.dim[1]; y++) {
			var pixel = matrix.getcell(x, y);
			var delta = pixel[1] + pixel[2] + pixel[3];
			if (delta > DELTA_THRESHOLD) {
				outlet(0, index);
				return;
			}
		}
	}
	outlet(0, -1);
}

function msg_int(sensitivity) {
	DELTA_THRESHOLD = sensitivity;
}