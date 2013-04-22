package fi.monoplan.fund.ui.model;

import java.io.Serializable;
import java.math.BigDecimal;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.xml.bind.annotation.XmlRootElement;

@SuppressWarnings("serial")
@Entity
@XmlRootElement
public class Member implements Serializable {

	@Id
	@GeneratedValue
	private Long id;

	private String fund;
	private String rating;
	private String currency;
	@Column(columnDefinition = "DECIMAL(12,4)")
	private BigDecimal nav;
	@Column(columnDefinition = "DECIMAL(12,4)")
	private BigDecimal day1;
	@Column(columnDefinition = "DECIMAL(12,4)")
	private BigDecimal month3;
	@Column(columnDefinition = "DECIMAL(12,4)")
	private BigDecimal month6;
	@Column(columnDefinition = "DECIMAL(12,4)")
	private BigDecimal year1;
	@Column(columnDefinition = "DECIMAL(12,4)")
	private BigDecimal year3;
	private String date;

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getFund() {
		return fund;
	}

	public void setFund(String fund) {
		this.fund = fund;
	}

	public String getRating() {
		return rating;
	}

	public void setRating(String rating) {
		this.rating = rating;
	}

	public String getCurrency() {
		return currency;
	}

	public void setCurrency(String currency) {
		this.currency = currency;
	}

	public BigDecimal getNav() {
		return nav;
	}

	public void setNav(BigDecimal nav) {
		this.nav = nav;
	}

	public BigDecimal getDay1() {
		return day1;
	}

	public void setDay1(BigDecimal day1) {
		this.day1 = day1;
	}

	public BigDecimal getMonth3() {
		return month3;
	}

	public void setMonth3(BigDecimal month3) {
		this.month3 = month3;
	}

	public BigDecimal getMonth6() {
		return month6;
	}

	public void setMonth6(BigDecimal month6) {
		this.month6 = month6;
	}

	public BigDecimal getYear1() {
		return year1;
	}

	public void setYear1(BigDecimal year1) {
		this.year1 = year1;
	}

	public BigDecimal getYear3() {
		return year3;
	}

	public void setYear3(BigDecimal year3) {
		this.year3 = year3;
	}

	public String getDate() {
		return date;
	}

	public void setDate(String date) {
		this.date = date;
	}

}
