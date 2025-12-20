#include <stdio.h>
#include <string.h>

int getRotation(char rotation[]) {


    // Transforming string to int
    int amount;
    // &rotation[1] skips first char 
    sscanf(&rotation[1], "%d", &amount);
    
    return amount;       
}


char getDirection(char rotation[]) {
    char direction = rotation[0];
    return direction;
}


void getNewIndex(int *start_idx, char direction, int amount, int array_size, int *count_ptr){
    // Pointer to current index
    int current = *start_idx;
    int count = amount / array_size;
    int rest = amount % array_size;
    
    // If "L" is used instead of 'L', C uses it as a pointer not char
    if (direction == 'L'){
        current = (current - rest + array_size) % array_size;
        if (rest > 0 && *start_idx != 0 && rest >= *start_idx) {
            count += 1;
        }
    }
    else if (direction == 'R') {
        current = (current + rest) % array_size;
        if (rest > 0 && *start_idx != 0 && (*start_idx + rest >= array_size)) {
            count += 1;
        }
    }
    else {
        printf("Direction input is neither L nor R");
    }
    // Change pointers instead of returning values
    *start_idx = current;
    *count_ptr += count;
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
            // Calculate new index and update counter
            getNewIndex(&current_idx, dir, rot, array_size, &counter);
        }
    }
    // Close file
    fclose(fptr);

    printf("Number of times dial pointed at 0 %d\n", counter);     
}

