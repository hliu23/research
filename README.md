# Research question: 

## Research procedure
- selecting languages
- selecting benchmarks
- selecting releases

- downloading available binaries
- setting up environment
- filtering versions likely to be compatible by hand
- running and benchmarking each release, with the power connected

- copying data from each release over by hand -> improve with script
- graphing the data and calculating Pearson's coefficient

## TODO
- organize the folder and disgard old data
- organize the scripts
- automate the process
- add more versions and more benchmarks and run again for python, recording procedure
- test out more languages (probably most time-consuming)
- graph and talk to Mr. Graham
- put all data into a Google Doc and write some paragraphs about it

### Actual procedure
- 20 most popular languages, 5 with benchmarks available
- language versions: well-known ones also used by other benchmarks: CPython, Node.js (uses v8 engine)
- benchmarks: five macrobenchmarks, test runs tell us that Havlak takes significantly more time to run
	- CD errors out in the code
- 15 runs because: required for some benchmarks (Havlak?), now need to be consistent across benchmarks?
- all releases numbers from website, exe downloaded long ago
- removed all python3 versions before 3.7, as well as all python2 versions from releases.txt because known incompatible with code
- remove installed versions from apps and programs
- prepared release.txt and env.conf, plugged in computer, cleared old data, restart
- installed python 3.6.8 to avoid collusion (w/o/ test suite or IDLE, add to path selected)
- no interference except checking on progress

### Data to present
- programming languages selected and basic characteristics? websites
- benchmarks and data on them
- actual graphs
- information about device?
- csv, then save as excel once final

#### Benchmarks
- average time to run on a quiet, unplugged pc, coefficient of variance with 15 runs: standard dev / mean
- python 3.11.2 - newest release at the time, relatively slower language
- selected benchmarks that are compatible
- selected benchmarks that are compatible
- selected benchmarks with mean run time under 5 seconds
	- time constraints
- coefficient of variation?
	- take data from DeltaBlue with a grain of salt
- 9 benchmarks selected: DeltaBlue Json Bounce List Permute Queens Sieve Storage Towers
- power disconnected at about 3.10.7, rerun if possible
- due to space limitations, only LTS versions are counted in NodeJS since they are the only types offered long-term support, and so should be equalivent to releases in other programs
- initial release at 2020
- statistics outliers detected for 3.9.11 and 3.9.10
#### Plan for data
- correlation and trendline for each, meet with all the data
- under .5 - weakly correlated


- 3.8.4 was collected while unplugged
- and 3.8.2 was disrupted
- rerun by changing release.txt, moving old data