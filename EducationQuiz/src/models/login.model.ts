export class LoginModel {
    constructor(public email: string, public password: string) { }
}
export class LoginErrorsModel {
    // tslint:disable-next-line: variable-name
    constructor(public email: [], public password: [], public non_field_errors: []) { }
}