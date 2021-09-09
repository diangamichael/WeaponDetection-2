import Navbar from 'react-bootstrap/Navbar'
import Container from 'react-bootstrap/Container'
import Nav from 'react-bootstrap/Nav'
import Icon from './AIIcon.png'


export default function NavigationBar() {
    return (
        <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
            <Container>
                <Navbar.Brand href="/">
                <img
                    id='icon'
                    alt=""
                    src={Icon}
                    width="50"
                    height="50"
                    className="d-inline-block align-top"
                />{' '}
                </Navbar.Brand>
                <Navbar.Brand href="/">
                    Weapon Detection
                </Navbar.Brand>
                <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                <Navbar.Collapse id="responsive-navbar-nav">
                <Nav className="me-auto">
                </Nav>
                <Nav>
                    <Nav.Link href="/info">How does it work?</Nav.Link>
                </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    )
}