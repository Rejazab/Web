import React, { Component } from "react";
import { Table } from "reactstrap";

class MainPage extends Component{
	render() {
		const informations = this.props.informations;
		return (
			<Table dark>
				<thead>
					<tr>
						<th>Last Name</th>
						<th>First Name</th>
						<th>Job</th>
						<th>mail</th>
						<th>linkedin</th>
						<th>github</th>
						<th>codingame</th>
						<th>language</th>
					</tr>
				</thead>
				<tbody>
				{!informations || informations.length <= 0 ?(
					<tr>
						<td colSpan="8" align="center">
							<b>No data to print yet</b>
						</td>
					</tr>
				) : (
					<tr>
						<td>{informations.last_name}</td>
						<td>{informations.first_name}</td>
						<td>{informations.job_title}</td>
						<td>{informations.mail}</td>
						<td>{informations.linkedin}</td>
						<td>{informations.github}</td>
						<td>{informations.codingame}</td>
						<td>{informations.languages}</td>
					</tr>
				)}
				</tbody>
			</Table>
		);
	}
}

export default MainPage;
