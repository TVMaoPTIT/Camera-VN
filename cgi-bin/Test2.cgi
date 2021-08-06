#!/usr/bin/perl


my $email = "lpatron\@stanford.edu";
my $reg_email = "";

print "Content-type: text/html\n\n";
print "<html>\n\n";
print "<head><title>test</title></head>\n";
print "<body>\n";

#print "$ENV{'SERVER_NAME'}<br>\n";

my $LOG = "log.dat";
my $time = localtime();
open (FILE, ">>$LOG") or die "Cannot open $LOG: $!";

if ($ENV{'SERVER_NAME'} =~ /\.stanford\.edu\/{0,1}/) {
  my $buffer = "";
  if ($ENV{'QUERY_STRING'} =~ /email/) {
    $buffer = $ENV{'QUERY_STRING'};
  } else {
    read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
  }
  my ($name, $value) = split(/=/, $buffer);
  if ($name eq "email"){
    $value =~ s/%([A-Za-z0-9]{2})/chr hex $1/ge;
    #$value =~ s/\+//g;
    $reg_email = $value;
  }
  if ($reg_email ne "") {
    `echo "$reg_email registered.  This is an automated notification.  Please do not reply" | mail -s "Request to join JGC mailing list" $email`;
    print FILE "$reg_email at $time\n";
    print "200 Success\n";
  } else { 
    print FILE "403 Error, invalid email\n";
    print "403 Error, invalid email\n";
  }
} else {
  print FILE "403 Error, invalid origin\n";
  print "403 Error, invalid origin\n";
}

close(FILE); 

print "</body>\n";
print "</html>";
