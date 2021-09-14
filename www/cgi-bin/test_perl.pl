#!/usr/bin/perl
print "Content-type: text/html\n\n";
print "Hello, World.<br><br>\n\n";
print "Test ok for cgi script written in Perl.<br><br>\n\n";

foreach my $key (keys %ENV) {
    print "$key --> $ENV{$key}<br>\n";
}

