//
//  User.swift
//
//
//  This file was auto-generated by Fern
//

import Foundation

public struct User: Codable {

    enum CodingKeys: String, CodingKey {
        case TEST = TEST
    }

    public let id: String
    public let name: String
    public let age: optional

}
