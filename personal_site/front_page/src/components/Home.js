import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import MainPage from "./MainPage";

import axios from "axios";
import { API_URL } from "../constants";

class Home extends Component{
	state = {
		informations: []
	};

	componentDidMount() {
		this.resetState();
	};

	getInformations = () => {
		axios.get(API_URL).then(res => this.setState({ informations: res.data }));
	};

	resetState = () => {
		this.getInformations();
	};

	render() {
		return (
			<Container style={{marginTop: "20px" }}>
				<Row>
					<Col>
						<MainPage
							informations={this.state.informations}
							resetState={this.resetState}
						/>
					</Col>
				</Row>
			</Container>
		);
	}
}

export default Home;