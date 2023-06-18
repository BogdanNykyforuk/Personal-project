import React from 'react';
import { Container, Typography, Link, Divider, Grid } from '@mui/material';
import { styled } from '@mui/system';
import signoutImage from '../images/signout.png';
import logo from '../images/logo.png';
import BGImage from '../images/background.jpg';


export const StyledContainer = styled(Container)(({ theme }) => ({
    backgroundColor: '#3d4d5c',
    color: '#e6e6e6',
    padding: theme.spacing(2),
    borderRadius: theme.spacing(1),
    marginTop: '50px',
    marginBottom: '110px'
  }));

export const StyledSubContainer = styled('div')(({ theme }) => ({
  backgroundColor: '#1c2833',
  padding: theme.spacing(2),
  borderRadius: theme.spacing(1),
}));

export const StyledDataItem = styled('div')(({ theme }) => ({
  marginBottom: theme.spacing(4),
  marginTop: theme.spacing(2),
}));

export const StyledDivider = styled(Divider)({
  width: '100%',
  height: '2px',
  backgroundColor: '#e6e6e6',
  marginBottom: '10px'
});

export const StyledLink = styled(Link)({
  color: '#e6e6e6',
  textDecoration: 'none',
  '&:hover': {
    color: '#90a7d5',
  },
});

export const StyledBackground = styled('div')({
    overflow: 'hidden',
    backgroundImage: `url(${BGImage})`,
    backgroundSize: 'cover',
});


const HeaderContainer = styled('header')({
backgroundColor: 'black',
padding: 0,
margin: 0,
});

const Nav = styled('nav')({
    ul: {
        marginRight: '20px',
        marginTop: 0,
        marginBottom: 0,
        padding: 0,
        listStyle: 'none',
        textAlign: 'right',
    },
    'ul li': {
        display: 'inline-block',
    },
    'ul li:last-child': {
        marginRight: 0,
    },
    'ul li a': {
        display: 'block',
        padding: '20px',
        color: 'white',
        textDecoration: 'none',
    },
    'ul li a img': {
        display: 'block',
        color: 'white',
        textDecoration: 'none',
    }
});

export const Header = ({ signOut }) => {
    return (
        <HeaderContainer>
        <Nav>
            <ul>
            <li style={{ textAlign: 'left', float: 'left' }}>
                <a href="/map">
                <img src={logo} style={{ width: '24px', height: '24px' }} />
                </a>
            </li>
            <li style={{ textAlign: 'left', float: 'left', transform: 'translateX(-20%)' }}>
                <a href="/map">SAFEROUTE</a>
            </li>
            <li className="navHover" style={{ textAlign: 'right' }}>
                <a href="/map">Map</a>
            </li>
            <li className="navHover" style={{ textAlign: 'right' }}>
                <a className="navHover" href="/about">About</a>
            </li>
            <li className="navHover" style={{ textAlign: 'right' }}>
                <a href="/used_data">Used data</a>
            </li>
            <li className="navHover" style={{ textAlign: 'right' }}>
                <a href="https://33faoddqwe4bjauetiiaatreye0uirjf.lambda-url.eu-central-1.on.aws/docs" target="_blank">SWAGGER UI</a>
            </li>
            <li className="navHover" style={{ textAlign: 'right' }}>
                <img
                className="navHover"
                src={signoutImage}
                alt="Signout"
                onClick={signOut}
                style={{ textAlign: 'right', cursor: 'pointer', width: '20px', height: '20px', transform: 'translateY(20%)' }}
                />
            </li>
            </ul>
        </Nav>
        </HeaderContainer>
    );
};