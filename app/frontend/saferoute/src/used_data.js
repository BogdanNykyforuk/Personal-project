import React from 'react';
import { withAuthenticator } from '@aws-amplify/ui-react';
import { Container, Typography, Link, Divider } from '@mui/material';
import {Header, StyledContainer, StyledSubContainer, StyledDataItem, StyledDivider, StyledLink} from './JS/ui_components';
import signoutImage from './images/signout.png';
import logo from './images/logo.png';


const UsedData = ({ signOut, user }) => {
  return (
    <>
      <Header>
        
      </Header>
      <StyledContainer>
        <StyledDataItem>
          <StyledSubContainer>
            <Typography variant="h6" component="h3" color="primary">
              <StyledLink href="https://hub.worldpop.org/geodata/summary?id=6545" target="_blank">Worldpop</StyledLink>
            </Typography>
            <StyledDivider />
            <Typography variant="body1">
              WorldPop (www.worldpop.org - School of Geography and Environmental Science, University of Southampton; Department of Geography and Geosciences, University of Louisville; 
              Departement de Geographie, Universite de Namur) and Center for International Earth Science Information Network (CIESIN), Columbia University (2018). 
              Global High Resolution Population Denominators Project - Funded by The Bill and Melinda Gates Foundation (OPP1134076).
            </Typography>
          </StyledSubContainer>
        </StyledDataItem>

        <StyledDataItem>
          <StyledSubContainer>
            <Typography variant="h6" component="h3" color="primary">
              <StyledLink href="https://catalog.data.gov/dataset/nypd-arrests-data-historic" target="_blank">Crime data</StyledLink>
            </Typography>
            <StyledDivider />
            <Typography variant="body1">
            List of every arrest in NYC going back to 2006 through the end of the previous calendar year. 
            This is a breakdown of every arrest effected in NYC by the NYPD going back to 2006 through the end of the previous calendar year. 
            This data is manually extracted every quarter and reviewed by the Office of Management Analysis and Planning before being posted on the NYPD website. 
            Each record represents an arrest effected in NYC by the NYPD and includes information about the type of crime, the location and time of enforcement. 
            In addition, information related to suspect demographics is also included. This data can be used by the public to explore the nature of police enforcement activity.
            </Typography>
          </StyledSubContainer>
        </StyledDataItem>

        <StyledDataItem>
          <StyledSubContainer>
            <Typography variant="h6" component="h3" color="primary">
              <StyledLink href="https://data.census.gov/table?q=b19013&g=040XX00US50$0600000&tid=ACSDT5Y2021.B19013&tp=true" target="_blank">Income data</StyledLink>
            </Typography>
            <StyledDivider />
            <Typography variant="body1">
            Original data came from here, but project used GEOCODIO to retrieve info from this table.
            </Typography>
          </StyledSubContainer>
        </StyledDataItem>
      </StyledContainer>
    </>
  );
};

export default withAuthenticator(UsedData, {
  socialProviders: ['google'],
});
