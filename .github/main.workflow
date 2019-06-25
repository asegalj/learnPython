workflow "IDENTIFIER" {
  on = "EVENT"
  resolves = "ACTION2"
}

action "ACTION1" {
 
}

action "ACTION2" {
  needs = "ACTION1"
  
}
