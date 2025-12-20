#include <stdio.h>
#include <string.h>

int getRotation(char rotation[]) {

    int len = strlen(rotation);
    // Create buffer for subset
    char temp[len];  
    for (int i = 1; i < len; i++){
        temp[i-1] = rotation[i];
    }
    // null-termination of string
    temp[len-1] = '\0';

    // Transforming string to int
    int amount;
    sscanf(temp, "%d", &amount);
    
    return amount;       
}


char getDirection(char rotation[]) {
    char direction = rotation[0];
    return direction;
}


int getNewIndex(int start_idx, char direction, int amount, int array_size){
    int idx = start_idx;
    // If "L" is used instead of 'L', C uses it as a pointer not char
    if (direction == 'L'){
        idx = (idx - amount) % array_size;
        if (idx < 0) {
            idx += array_size;
        }
    }
    else if (direction == 'R') {
        idx = (idx + amount) % array_size;
    }
    else {
        printf("Direction input is neither L nor R");
    }

    return idx;
}


int main() {
    int array_size = 100;
    // Starting index provided by instructions
    int current_idx = 50;
    int counter = 0;

    // Read rotation inputs from local file
    FILE *fptr = fopen("day_1_rotations", "r");

    if (fptr == NULL) {
        printf("Error: Could not open file.\n");
        return 1;
    }

    char buffer[50];

    // File length is unknown -> read line by line and make calculaions on the fly
    while (fgets(buffer, 50, fptr)) {
        // Remove line break in case it exists
        buffer[strcspn(buffer, "\n")] = 0;

        if (strlen(buffer) > 0) {
            int rot = getRotation(buffer);
            char dir = getDirection(buffer);
            // Calculate new index
            current_idx = getNewIndex(current_idx, dir, rot, array_size);

            if (current_idx == 0) {
                counter++;
            }
        }
    }
    // Close file
    fclose(fptr);

    printf("Number of times dial pointed at 0 %d\n", counter);
         
}

