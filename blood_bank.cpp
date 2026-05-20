#include <stdio.h>
#include <string.h>

struct BloodDonation {
    int id;
    char bloodType[4];
    int units;
    char city[50];
    char donorName[50];
    char contact[20];
    char status[15];
};

struct BloodRequest {
    int id;
    char requiredType[4];
    int unitsNeeded;
    char hospital[50];
    char urgency[20];
};

int canDonateTo(char *donorType, char *recipientType)
{
    if (strcmp(donorType, "O-") == 0)
        return 1;

    if (strcmp(donorType, "O+") == 0) {
        if (strcmp(recipientType, "O+") == 0 ||
            strcmp(recipientType, "A+") == 0 ||
            strcmp(recipientType, "B+") == 0 ||
            strcmp(recipientType, "AB+") == 0)
            return 1;
    }

    if (strcmp(donorType, "A-") == 0) {
        if (strcmp(recipientType, "A-") == 0 ||
            strcmp(recipientType, "A+") == 0 ||
            strcmp(recipientType, "AB-") == 0 ||
            strcmp(recipientType, "AB+") == 0)
            return 1;
    }

    if (strcmp(donorType, "A+") == 0) {
        if (strcmp(recipientType, "A+") == 0 ||
            strcmp(recipientType, "AB+") == 0)
            return 1;
    }

    if (strcmp(donorType, "B-") == 0) {
        if (strcmp(recipientType, "B-") == 0 ||
            strcmp(recipientType, "B+") == 0 ||
            strcmp(recipientType, "AB-") == 0 ||
            strcmp(recipientType, "AB+") == 0)
            return 1;
    }

    if (strcmp(donorType, "B+") == 0) {
        if (strcmp(recipientType, "B+") == 0 ||
            strcmp(recipientType, "AB+") == 0)
            return 1;
    }

    if (strcmp(donorType, "AB-") == 0) {
        if (strcmp(recipientType, "AB-") == 0 ||
            strcmp(recipientType, "AB+") == 0)
            return 1;
    }

    if (strcmp(donorType, "AB+") == 0) {
        if (strcmp(recipientType, "AB+") == 0)
            return 1;
    }

    return 0;
}

int main()
{
    char donor[4], recipient[4];

    printf("Enter donor blood group: ");
    scanf("%3s", donor);

    printf("Enter recipient blood group: ");
    scanf("%3s", recipient);

    if (canDonateTo(donor, recipient))
        printf("Compatible: Donor can donate.\n");
    else
        printf("Not Compatible: Donor cannot donate.\n");

    return 0;
}
