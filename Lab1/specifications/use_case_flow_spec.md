# Use Case Flow Specification
**Use Case:** UC-03 - Book Confidential Counseling Session  
**SRN:** PES2UG24CS016 | **System:** Corporate Mental Wellness & Counseling Platform

---

### Basic Details
- **Use Case ID:** UC-03
- **Name:** Book Confidential Counseling Session
- **Primary Actor:** Corporate Employee
- **Secondary Actor:** Licensed Therapist
- **Other Systems:** Timezone Engine, Anonymization Service
- **Priority:** High
- **Frequency:** High (whenever employee wants to book)

### Description
This use case explains how an employee books a confidential session with a therapist. The employee searches for therapists, checks available slots (converted to their local timezone), and confirms booking. The whole process uses only the pseudo-ID (EMP-XXXX) so that real identity is not revealed to the therapist.

### Preconditions
1. Employee is logged in via company SSO.
2. Pseudo-ID service is working.
3. Therapists have updated their availability calendar.

### Postconditions
1. Slot is booked and saved in the system.
2. Meeting link + calendar invite (with pseudo-ID only) sent to both employee and therapist.
3. No real employee details are shown anywhere in the booking.

### Trigger
Employee clicks "Schedule Confidential Session" on the dashboard (or is redirected after a high stress score in UC-02).

---

### Main Success Scenario

| Step | What User Does | What System Does |
| :--- | :--- | :--- |
| 1 | Employee clicks "Book Counseling Session" | System starts booking flow and includes UC-01 (Generate Pseudo-ID) |
| 2 | Employee agrees to anonymous mode | System gives/verifies pseudo-ID like EMP-7F89X |
| 3 | Employee filters therapists by specialization, language etc. | System shows matching therapist profiles |
| 4 | Employee selects a therapist | System fetches available slots and includes UC-08 (Validate Timezone & Slot Availability) to show time in employee's local timezone |
| 5 | Employee picks a date & time slot | System locks the slot for 5 minutes temporarily and shows booking summary with pseudo-ID |
| 6 | Employee confirms booking | System checks lock is still valid and saves booking in DB |
| 7 | - | System creates encrypted video meeting link linked to pseudo-ID |
| 8 | - | System sends calendar invites to employee (in portal) and therapist dashboard |
| 9 | - | System updates therapist's availability |
| 10 | Employee sees confirmation page | System shows meeting link and option to add to calendar. End of use case. |

---

### Alternate Flows

**Alternate Flow 5a - Slot already taken (conflict):**
- 5a1. While employee is selecting, someone else books the same slot.
- 5a2. System finds conflict during UC-08 check and releases the temporary lock.
- 5a3. Shows message: "Sorry, this slot was just booked. Please choose another time."
- 5a4. Employee picks a different slot, continue from Step 5.

**Alternate Flow 8a - User cancels (extends UC-10):**
- 8a1. At confirmation step, employee clicks "Cancel".
- 8a2. System calls extend UC-10 (Reschedule/Cancel Booking).
- 8a3. Releases the 5-min lock and makes slot available again.
- 8a4. Shows "Booking cancelled. Nothing was saved." End of flow.

**Exception Flow 2a - High stress score alert (extends UC-09):**
- 2a1. If employee came from UC-02 with GAD-7 score >=15 (severe).
- 2a2. System triggers extend UC-09 (Emergency Crisis Protocol).
- 2a3. Shows 24/7 crisis helpline banner along with booking options.

---
*End of UC-03 Specification - 1 page version for submission*
