/* eslint-disable @typescript-eslint/no-extraneous-class */
export default class Utils {

  public static fileHeaderGenerator(filename: string, ): string {
    return `
//
//  ${filename}.swift
//
//
//  This file was auto-generated by Fern
//
        `.trim();
  }

}