# Cache Protocol Simulator Tests

### Credits

### Tests

1. Generate the analysis traces by runnin `./run_pintool.sh` in the root folder.

2. Go to the folder of the Cache Simulator with `cd CacheSim` and compile the simulator by runnin `make`

3. Run the simulator with this command `./cache_sim [-c <Number of cores>] [-s <Cache_size in MB>] [-a <Set Associativity>] [-p <Cache Coherence Protocol>] [-t <Trace File>]`

For example: `./run_cacheSim -c 16 -s 1024 -a 8 -p MSI -t ../traces/MSIvMESI.trace` this will run the trace named MSIvMESI.trace by appliying the protocol MSI with an associativity of 8 and 16 cores.

At the end of the program you will find the stadistics of the test shown this way:

Total Acceses = 32000
Bus Transactions = 32000
Memory Requests = 16000
Memory Write Backs = 0
Cache Transfers = 0