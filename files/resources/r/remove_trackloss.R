remove_trackloss <- function(data='', subject_col='', trial_col='', trackloss_col='', threshold=0.5){
  # print start
  print(paste('Removing trackloss trials from...', deparse(substitute(data)), sep = ' '))
  
  # create an empty data frame to store track loss trials
  dat_exclude <- data.frame(matrix(ncol=3,nrow=0))
  c <- c(subject_col, trial_col, 'exclude')
  colnames(dat_exclude) <- c
  
  # get the number of the columns of interest
  participant_n <- which(colnames(data)==subject_col)
  trial_n <- which(colnames(data)==trial_col)
  trackloss_n <- which(colnames(data)==trackloss_col)
  
  # order the data frame by subject and trial
  data <- data[with(data, order(data[,participant_n], data[,trial_n])), ]
  
  # loop through all observations to determine whether each trial is a track loss trial
  participant <- as.vector(data[,participant_n])[1] # find the first trial
  trial <- as.numeric(as.vector(data[,trial_n])[1]) # find the first participant
  x <- 0
  y <- 0
  for (i in 1:nrow(data)) {
    if (i == nrow(data)) { # if the last row (to include the last trial)
      x=x+1
      if (data[i, trackloss_n] == 0) {
        y=y+1
      }
      ex <- (y>x*threshold)
      new_row <- c(participant, trial, ex)
      dat_exclude[nrow(dat_exclude)+1,] = new_row
    } else if (data[i, trial_n] ==  trial & data[i, participant_n] == participant) { # if same participant in the same trial
      x=x+1
      if (data[i, trackloss_n] == 0) {
        y=y+1
      }
    } else { # if new trial or new participant
      ex <- (y>x*threshold)
      new_row <- c(participant, trial, ex)
      dat_exclude[nrow(dat_exclude)+1,] = new_row
      trial = as.numeric(as.vector(data[,trial_n])[i])
      participant = as.character(as.vector(data[,participant_n])[i])
      x=0
      y=0
    }
  }
  
  # print summary
  print(paste('exluded number of trials:', length(which(dat_exclude$exclude==TRUE)), sep = ' '))
  print(paste('out of number of trials:', nrow(dat_exclude), sep = ' '))
  print(paste('excluded percentage: ', (length(which(dat_exclude$exclude==TRUE))/nrow(dat_exclude))*100, "%", sep = ''))
  print(paste('number of trials remaining:', (nrow(dat_exclude)-length(which(dat_exclude$exclude==TRUE))), sep = ' '))
  
  # create and return the cleaned data frame
  data_cleaned <- merge(data, dat_exclude, by = c(subject_col, trial_col))
  data_cleaned <- droplevels(subset(data_cleaned, exclude == FALSE))
  data_cleaned <- data_cleaned[ , -which(names(data_cleaned) == 'exclude')]
  return(data_cleaned)
}