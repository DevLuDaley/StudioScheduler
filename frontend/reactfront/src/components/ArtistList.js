import React, { Component } from "react";
import { Table } from "reactstrap";
import NewArtistModal from "./NewArtistModal";
import { getArtists } from ".frontend/reactfront/src/components/Home.js";

import ConfirmRemovalModal from "./ConfirmRemovalModal";

class ArtistList extends Component {
  render() {
    const artists = this.props.artists;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>Name</th>
            <th>Location</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!artists || artists.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Oops, no data loaded here yet</b>
              </td>
            </tr>
          ) : (
            artists.map(artist => (
              <tr key={artist.pk}>
                <td>{artist.name}</td>
                <td>{artist.location}</td>
                <td align="center">
                  <NewArtistModal
                    create={false}
                    artist={artist}
                    resetState={this.props.resetState}
                  />
                  &nbsp;&nbsp;
                  <ConfirmRemovalModal
                    pk={artist.pk}
                    resetState={this.props.resetState}
                  />
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default ArtistList;
