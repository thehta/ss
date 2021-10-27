# SU Study Centre Utils
See the available seats in the SS, and book one.

## Usage:
```bash
python ss.py get 'YYYY-MM-DD' 'HH:00'
```
```bash
python ss.py book 'YYYY-MM-DD' 'HH:00' 'D1-<seat_no>' 'SU_id' 'name'
```     
## Examples:            
Get all available seats for 9 am on October 30th:
```bash
python ss.py get '2021-10-30' '09:00'
```

Book seat D53 at 9 am on October 30th for Thomas:
```bash
python ss.py book '2021-10-30' '09:00' 'D1-53' '12345678' 'Thomas'
```