#!/usr/bin/perl
use warnings;
use strict;

if ($#ARGV != 2) {
	die "Usage: ./maketest threshold=[0-1] questions.txt termfreq.txt\n";
}

srand(time());

my $threshold = $ARGV[0];

open QFH, "<".$ARGV[1];
open TFH, "<".$ARGV[2];

open QtestFH, ">questions_test.txt";
open QtrainFH, ">questions_train.txt";
open TtrainFH, ">termfreq_train.txt";

# For each line in the topics file
while (<TFH>) {
	
	# Read the corresponding question
	my $qline1 = <QFH>;
	my $qline2 = <QFH>;
	my $qline3 = <QFH>;

	# Put random questions in the test and training files
	if (rand() > $threshold) {
		print TtrainFH $_;
		print QtrainFH $qline1;
		print QtrainFH $qline2;
		if (defined($qline3)) { print QtrainFH $qline3; }
	} else {
		print QtestFH $qline1;
		print QtestFH $qline2;
		if (defined($qline3)) { print QtestFH $qline3; }
	}

}

close(QFH);
close(TFH);
close(QtestFH);
close(QtrainFH);
close(TtrainFH);
