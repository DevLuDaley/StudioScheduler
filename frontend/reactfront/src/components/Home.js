import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import ArtistList from "./ArtistList";
import NewArtistModal from "./NewArtistModal";

import axios from "axios";

import { API_URL } from "../constants";

class Home extends Component {
  state = {
    artists: []
  };

  componentDidMount() {
    this.resetState();
  }

  getArtists = () => {
    axios
      .get(API_URL)
      // .get(`http://127.0.0.1:8000/api/v1/artists/`)
      .then(res => this.setState({ artists: res.data.conversations }));
    //      .then(res => this.setState({ artists: res.data.conversations }));
    //      console.log(this);
    // console.log(res);
  };

  resetState = () => {
    this.getArtists();
  };

  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            <ArtistList
              artists={this.state.artists}
              resetState={this.resetState}
            />
          </Col>
        </Row>
        <Row>
          <Col>
            <NewArtistModal create={true} resetState={this.resetState} />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Home;
